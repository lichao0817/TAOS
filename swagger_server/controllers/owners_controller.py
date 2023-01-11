import base64
import connexion
import pickle
import six
import sqlite3

from swagger_server.models.form_assignment import FormAssignment
from swagger_server.models.form_template import FormTemplate
from swagger_server.models.option import Option
from swagger_server.models.question import Question
from swagger_server import util


def add_form(body, owner_id):
    """Add a form for owner

    :param body: add a new questionaire template
    :type body: dict | bytes
    :param owner_id: ID of form to return
    :type owner_id: int

    :rtype: FormTemplate
    """
    if connexion.request.is_json:
        body = FormTemplate.from_dict(connexion.request.get_json())
        conn = util.get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO form_templates (owner_id, title, description) VALUES (?, ?, ?)",
                    (owner_id, body.title, body.description)
                    )
        cur.execute("select last_insert_rowid()")
        template_id = cur.fetchone()[0]
        index = 1
        for question in body.questions:
            cur.execute("INSERT INTO questions (question_index, template_id, description, type) VALUES (?, ?, ?, ?)",
                        (index, template_id, question.description, question.type)
                        )
            cur.execute("select last_insert_rowid()")
            if question.type != 'text':
                question_id = cur.fetchone()[0]
                for option in question.options:
                    cur.execute("INSERT INTO options (option_index, question_id, description) VALUES (?, ?, ?)",
                                (option.option_index, question_id, option.description)
                                )
            index += 1
        conn.commit()
        return template_id
    return "Invalid request"


def assign_new_forms_to_client(owner_id, client_id):
    """Assign new forms to client

    :param owner_id: ID of owner
    :type owner_id: int
    :param client_id: ID of client
    :type client_id: int

    :rtype: List[Integer] list of assignment IDs
    """
    if connexion.request.is_json:
        forms = connexion.request.get_json()['forms']
        conn = util.get_db_connection()
        cur = conn.cursor()
        assignment_ids = []
        for form in forms:
            # Check if the form is already assigned
            vals = cur.execute("SELECT * FROM form_assignments WHERE owner_id=? AND client_id=? AND template_id=?", (owner_id, client_id, form)).fetchone()
            if not vals:
                cur.execute("INSERT INTO form_assignments (owner_id, client_id, template_id) VALUES (?, ?, ?)",
                        (owner_id, client_id, form)
                        )
                cur.execute("select last_insert_rowid()")
                assignment_ids.append(cur.fetchone()[0])
        conn.commit()
        return assignment_ids
    return "Invalid request"


def find_all_assignments_for_client(owner_id, client_id):
    """Find all the assigned forms and their status for clients

    :param owner_id: ID of owner
    :type owner_id: int
    :param client_id: ID of client
    :type client_id: int

    :rtype: List[FormAssignment]
    """
    conn = util.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM form_assignments WHERE owner_id=? AND client_id=?",
                (owner_id, client_id))
    assignments = [FormAssignment.from_dict(
        dict(row)) for row in cur.fetchall()]
    return assignments


def get_all_forms_for_owner(owner_id):
    """Find all form templates for an owner

    Returns the summary list of the forms

    :param owner_id: ID of owner to return
    :type owner_id: int

    :rtype: List[FormTemplate]
    """
    conn = util.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM form_templates WHERE owner_id=?", (owner_id,))
    template_query_list = cur.fetchall()
    templates = [FormTemplate.from_dict(dict(row))
                 for row in template_query_list]
    return templates


def get_form_for_owner(owner_id, template_id):
    """Find the form with formId for an owner

    Returns a single form with the form ID for owner

    :param owner_id: ID of the owner
    :type owner_id: int
    :param template_id: ID of form template to return
    :type template_id: int

    :rtype: FormTemplate
    """
    conn = util.get_db_connection()
    cur = conn.cursor()
    # Fetch the form template
    cur.execute("SELECT * FROM form_templates WHERE owner_id=? AND id=?",
                (owner_id, template_id))
    template = FormTemplate.from_dict(dict(cur.fetchone()))
    # Fetch all questions from the template
    cur.execute("SELECT * FROM questions WHERE template_id=?", (template_id,))
    questions = [Question.from_dict(dict(question))
                 for question in cur.fetchall()]
    for question in questions:
        if question.type != 'text':
            cur.execute(
                "SELECT * FROM options WHERE question_id=?", (question.id,))
            question.options = [Option.from_dict(
                dict(question)) for question in cur.fetchall()]

    template.questions = questions
    return template
