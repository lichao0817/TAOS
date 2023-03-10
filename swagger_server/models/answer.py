# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Answer(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, question_id: int=None, response_id: int=None, client_id: int=None, template_id: int=None, created_at: str=None, last_modify: str=None, type: str=None, response: str=None):  # noqa: E501
        """Answer - a model defined in Swagger

        :param id: The id of this Answer.  # noqa: E501
        :type id: int
        :param question_id: The question_id of this Answer.  # noqa: E501
        :type question_id: int
        :param response_id: The response_id of this Answer.  # noqa: E501
        :type response_id: int
        :param client_id: The client_id of this Answer.  # noqa: E501
        :type client_id: int
        :param template_id: The template_id of this Answer.  # noqa: E501
        :type template_id: int
        :param created_at: The created_at of this Answer.  # noqa: E501
        :type created_at: str
        :param last_modify: The last_modify of this Answer.  # noqa: E501
        :type last_modify: str
        :param type: The type of this Answer.  # noqa: E501
        :type type: str
        :param response: The response of this Answer.  # noqa: E501
        :type response: str
        """
        self.swagger_types = {
            'id': int,
            'question_id': int,
            'response_id': int,
            'client_id': int,
            'template_id': int,
            'created_at': str,
            'last_modify': str,
            'type': str,
            'response': str
        }

        self.attribute_map = {
            'id': 'id',
            'question_id': 'questionId',
            'response_id': 'responseId',
            'client_id': 'clientId',
            'template_id': 'templateId',
            'created_at': 'createdAt',
            'last_modify': 'lastModify',
            'type': 'type',
            'response': 'response'
        }
        self._id = id
        self._question_id = question_id
        self._response_id = response_id
        self._client_id = client_id
        self._template_id = template_id
        self._created_at = created_at
        self._last_modify = last_modify
        self._type = type
        self._response = response

    @classmethod
    def from_dict(cls, dikt) -> 'Answer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Answer of this Answer.  # noqa: E501
        :rtype: Answer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Answer.


        :return: The id of this Answer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Answer.


        :param id: The id of this Answer.
        :type id: int
        """

        self._id = id

    @property
    def question_id(self) -> int:
        """Gets the question_id of this Answer.


        :return: The question_id of this Answer.
        :rtype: int
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id: int):
        """Sets the question_id of this Answer.


        :param question_id: The question_id of this Answer.
        :type question_id: int
        """

        self._question_id = question_id

    @property
    def response_id(self) -> int:
        """Gets the response_id of this Answer.


        :return: The response_id of this Answer.
        :rtype: int
        """
        return self._response_id

    @response_id.setter
    def response_id(self, response_id: int):
        """Sets the response_id of this Answer.


        :param response_id: The response_id of this Answer.
        :type response_id: int
        """

        self._response_id = response_id

    @property
    def client_id(self) -> int:
        """Gets the client_id of this Answer.


        :return: The client_id of this Answer.
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: int):
        """Sets the client_id of this Answer.


        :param client_id: The client_id of this Answer.
        :type client_id: int
        """

        self._client_id = client_id

    @property
    def template_id(self) -> int:
        """Gets the template_id of this Answer.


        :return: The template_id of this Answer.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id: int):
        """Sets the template_id of this Answer.


        :param template_id: The template_id of this Answer.
        :type template_id: int
        """

        self._template_id = template_id

    @property
    def created_at(self) -> str:
        """Gets the created_at of this Answer.


        :return: The created_at of this Answer.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        """Sets the created_at of this Answer.


        :param created_at: The created_at of this Answer.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def last_modify(self) -> str:
        """Gets the last_modify of this Answer.


        :return: The last_modify of this Answer.
        :rtype: str
        """
        return self._last_modify

    @last_modify.setter
    def last_modify(self, last_modify: str):
        """Sets the last_modify of this Answer.


        :param last_modify: The last_modify of this Answer.
        :type last_modify: str
        """

        self._last_modify = last_modify

    @property
    def type(self) -> str:
        """Gets the type of this Answer.

        the question type  # noqa: E501

        :return: The type of this Answer.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Answer.

        the question type  # noqa: E501

        :param type: The type of this Answer.
        :type type: str
        """
        allowed_values = ["text", "single", "multiple"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def response(self) -> str:
        """Gets the response of this Answer.

        The response will be used for all types of questions.  # noqa: E501

        :return: The response of this Answer.
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response: str):
        """Sets the response of this Answer.

        The response will be used for all types of questions.  # noqa: E501

        :param response: The response of this Answer.
        :type response: str
        """

        self._response = response
