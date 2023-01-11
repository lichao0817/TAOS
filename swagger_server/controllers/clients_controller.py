import connexion
import six

from swagger_server import util


def complete_form_for_client(user_id, form_id):  # noqa: E501
    """Modify the form with the formId

     # noqa: E501

    :param user_id: ID of owner to return
    :type user_id: int
    :param form_id: ID of form to return
    :type form_id: int

    :rtype: None
    """
    return 'do some magic!'


def find_form_for_client(user_id, form_id):  # noqa: E501
    """Find the form with formId for an owner

    Returns a single form with the form ID for owner # noqa: E501

    :param user_id: ID of owner to return
    :type user_id: int
    :param form_id: ID of form to return
    :type form_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_forms_for_client(user_id):  # noqa: E501
    """Find all forms assigned to a client

    Returns a single pet # noqa: E501

    :param user_id: ID of owner to return
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'
