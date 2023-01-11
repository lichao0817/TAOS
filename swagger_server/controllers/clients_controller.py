import connexion
import six

from swagger_server.models.form_assignment import FormAssignment
from swagger_server.models.form_response import FormResponse
from swagger_server.models.form_template import FormTemplate
from swagger_server.models.option import Option
from swagger_server.models.question import Question
from swagger_server import util


def complete_form_for_client(user_id, form_id):
    """Modify the form with the formId

    :param user_id: ID of owner to return
    :type user_id: int
    :param form_id: ID of form to return
    :type form_id: int

    :rtype: Integer the id of created response
    """
    if connexion.request.is_json:
        body = FormResponse.from_dict(connexion.request.get_json())
        conn = util.get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM form_templates WHERE id=?",
                (form_id,))
        # Fetch the form template
        template = FormTemplate.from_dict(dict(cur.fetchone()))
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
        template.questions = questions
        
        if len(questions) != body.answers:
            return "Not all questions have answers"

        cur.execute("INSERT INTO form_responses (client_id, template_id) VALUES (?, ?)",
                    (user_id, form_id)
                    )
        cur.execute("select last_insert_rowid()")
        response_id = cur.fetchone()[0]
        for answer in body.answers:
            cur.execute("INSERT INTO answers (question_id, template_id, type, response) VALUES (?, ?, ?, ?)",
                        (answer.question_id, answer.template_id, answer.type, answer.response)
                        )
            cur.execute("select last_insert_rowid()")
            answer_id = cur.fetchone()[0]
        # Check if the form is complete
        conn.commit()
        return template_id
    return "Invalid request"


def find_form_for_client(user_id, form_id):
    """Find the form with formId for an owner

    Returns a single form with the form ID for owner # noqa: E501

    :param user_id: ID of owner to return
    :type user_id: int
    :param form_id: ID of form to return
    :type form_id: int

    :rtype: None
    """
    conn = util.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM form_responses WHERE client_id=? AND template_id=?",
                (user_id, form_id))
    response = FormResponse.from_dict(dict(cur.fetchone))
    return response


def get_all_forms_for_client(user_id):
    """Find all forms assigned to a client

    Returns all form assignments for a client (from different owners)

    :param user_id: ID of owner to return
    :type user_id: int

    :rtype: List[FormAssignment]
    """
    conn = util.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM form_assignments WHERE client_id=?",
                (user_id,))
    assignments = [FormAssignment.from_dict(
        dict(row)) for row in cur.fetchall()]
    return assignments
