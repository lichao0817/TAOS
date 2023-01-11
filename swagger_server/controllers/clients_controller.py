import connexion
import six

from swagger_server.models.form_assignment import FormAssignment
from swagger_server.models.form_response import FormResponse
from swagger_server.models.form_template import FormTemplate
from swagger_server.models.answer import Answer
from swagger_server.models.option import Option
from swagger_server.models.question import Question
from swagger_server import util


def complete_form_for_client(client_id, form_id):
    """Modify the form with the formId

    :param client_id: ID of owner to return
    :type client_id: int
    :param form_id: ID of form to return
    :type form_id: int

    :rtype: Integer the id of created response
    """
    if connexion.request.is_json:
        body = FormResponse.from_dict(connexion.request.get_json())
        conn = util.get_db_connection()
        cur = conn.cursor()
        # Fetch all questions from the template
        cur.execute("SELECT * FROM questions WHERE template_id=?", (form_id,))
        questions = [Question.from_dict(dict(question))
                     for question in cur.fetchall()]
        for question in questions:
            if question.type != 'text':
                cur.execute(
                    "SELECT * FROM options WHERE question_id=?", (question.id,))
                question.options = [Option.from_dict(
                    dict(question)) for question in cur.fetchall()]

        answers = body.answers
        questions.sort(key=getIndex)
        answers.sort(key=getIndex)
        
        if len(questions) != answers:
            return "Not all questions have answers"
        for (question, answer) in zip(questions, answers):
            if question.type != answer.type or question.id != answer.question_id:
                return "The question and its answer doesn't match"

        cur.execute("INSERT INTO form_responses (client_id, template_id) VALUES (?, ?)",
                    (client_id, form_id)
                    )
        cur.execute("select last_insert_rowid()")
        response_id = cur.fetchone()[0]
        for answer in body.answers:
            cur.execute("INSERT INTO answers (question_id, response_id, template_id, type, response) VALUES (?, ?, ?, ?, ?)",
                        (answer.question_id, response_id,
                         answer.template_id, answer.type, answer.response)
                        )
        cur.execute("UPDATE form_assignments SET status='complete' WHERE client_id=? AND template_id=?",
                    ('complete', client_id, form_id))
        conn.commit()
        return response_id
    return "Invalid request"


def find_form_response_for_client(client_id, form_id):
    """Find the form with formId for an owner

    Returns a single form with the form ID for owner # noqa: E501

    :param client_id: ID of owner to return
    :type client_id: int
    :param form_id: ID of form to return
    :type form_id: int

    :rtype: None
    """
    conn = util.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM form_responses WHERE client_id=? AND template_id=?",
                (client_id, form_id))
    response = FormResponse.from_dict(dict(cur.fetchone))
    return response


def get_all_forms_for_client(client_id):
    """Find all forms assigned to a client

    Returns all form assignments for a client (from different owners)

    :param client_id: ID of owner to return
    :type client_id: int

    :rtype: List[FormAssignment]
    """
    conn = util.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM form_assignments WHERE client_id=?",
                (client_id,))
    assignments = [FormAssignment.from_dict(
        dict(row)) for row in cur.fetchall()]
    return assignments

def getIndex(element):
  if isinstance(element, Question):
    return element.id
  return element.question_id
