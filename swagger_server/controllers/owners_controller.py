import base64
import connexion
import pickle
import six
import sqlite3

from swagger_server.models.form_template import FormTemplate  # noqa: E501
from swagger_server import util


def add_form(body, user_id):  # noqa: E501
    """Add a form for owner

     # noqa: E501

    :param body: add a new questionaire template
    :type body: dict | bytes
    :param user_id: ID of form to return
    :type user_id: int

    :rtype: FormTemplate
    """
    if connexion.request.is_json:
        body = FormTemplate.from_dict(connexion.request.get_json())  # noqa: E501
        conn = util.get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO form_templates (owner_id, title, description) VALUES (?, ?, ?)",
                    (user_id, body.title, body.description)
                    )
        cur.execute("select last_insert_rowid()")
        template_id = cur.fetchone()[0]
        index = 1
        for question in body.questions:
            cur.execute("INSERT INTO questions (question_index, template_id, description, type) VALUES (?, ?, ?, ?)",
                            (index, template_id, question.description, question.type)
                            )
            cur.execute("select last_insert_rowid()")
            question_id = cur.fetchone()[0]
            index += 1
        conn.commit()
    return template_id

def find_all_clients_for_owner(owner_id):  # noqa: E501
    """Find all clients for an owner

     # noqa: E501

    :param owner_id: ID of owner
    :type owner_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_forms_for_owner(user_id):  # noqa: E501
    """Find all form templates for an owner

    Returns a single pet # noqa: E501

    :param user_id: ID of owner to return
    :type user_id: int

    :rtype: List[FormTemplate]
    """
    conn = util.get_db_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM form_templates WHERE owner_id=?", (user_id,))
    template_query_list = cur.fetchall()
    templates = [FormTemplate.from_dict(dict(row)) for row in template_query_list]
    return templates


def get_form_for_owner(user_id, template_id):  # noqa: E501
    """Find the form with formId for an owner

    Returns a single form with the form ID for owner # noqa: E501

    :param user_id: ID of the owner
    :type user_id: int
    :param template_id: ID of form template to return
    :type template_id: int

    :rtype: FormTemplate
    """
    conn = util.get_db_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # Fetch the form template
    cur.execute("SELECT * FROM form_templates WHERE owner_id=? AND id=?", (user_id, template_id))
    template = FormTemplate.from_dict(dict(cur.fetchone()))
    # Fetch all questions from the template
    cur.execute("SELECT * FROM questions WHERE template_id=?", (template_id))
    question_dicts = [dict(question) for question in cur.fetchall()]
    questions = []
    for question_dict in question_dicts:
        if question_dict['type'] == 'freeText':
            question_dict['options'] = []
        else:
            option_encoded_txt = base64_bytes.decode('ascii')
            message_bytes = pickle.dumps(question.options)
            base64_bytes = base64.b64encode(message_bytes)
            
    template.questions = questions
    return template


def get_owner_by_id(user_id):  # noqa: E501
    """Find owner by ID

    Returns a single pet # noqa: E501

    :param user_id: ID of owner to return
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'
