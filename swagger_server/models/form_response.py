# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.answer import Answer  # noqa: F401,E501
from swagger_server import util


class FormResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, client_id: int=None, template_id: int=None, created_at: str=None, last_modify: str=None, answers: List[Answer]=None):  # noqa: E501
        """FormResponse - a model defined in Swagger

        :param id: The id of this FormResponse.  # noqa: E501
        :type id: int
        :param client_id: The client_id of this FormResponse.  # noqa: E501
        :type client_id: int
        :param template_id: The template_id of this FormResponse.  # noqa: E501
        :type template_id: int
        :param created_at: The created_at of this FormResponse.  # noqa: E501
        :type created_at: str
        :param last_modify: The last_modify of this FormResponse.  # noqa: E501
        :type last_modify: str
        :param answers: The answers of this FormResponse.  # noqa: E501
        :type answers: List[Answer]
        """
        self.swagger_types = {
            'id': int,
            'client_id': int,
            'template_id': int,
            'created_at': str,
            'last_modify': str,
            'answers': List[Answer]
        }

        self.attribute_map = {
            'id': 'id',
            'client_id': 'clientId',
            'template_id': 'templateId',
            'created_at': 'createdAt',
            'last_modify': 'lastModify',
            'answers': 'answers'
        }
        self._id = id
        self._client_id = client_id
        self._template_id = template_id
        self._created_at = created_at
        self._last_modify = last_modify
        self._answers = answers

    @classmethod
    def from_dict(cls, dikt) -> 'FormResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FormResponse of this FormResponse.  # noqa: E501
        :rtype: FormResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this FormResponse.


        :return: The id of this FormResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this FormResponse.


        :param id: The id of this FormResponse.
        :type id: int
        """

        self._id = id

    @property
    def client_id(self) -> int:
        """Gets the client_id of this FormResponse.


        :return: The client_id of this FormResponse.
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: int):
        """Sets the client_id of this FormResponse.


        :param client_id: The client_id of this FormResponse.
        :type client_id: int
        """

        self._client_id = client_id

    @property
    def template_id(self) -> int:
        """Gets the template_id of this FormResponse.


        :return: The template_id of this FormResponse.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id: int):
        """Sets the template_id of this FormResponse.


        :param template_id: The template_id of this FormResponse.
        :type template_id: int
        """

        self._template_id = template_id

    @property
    def created_at(self) -> str:
        """Gets the created_at of this FormResponse.


        :return: The created_at of this FormResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        """Sets the created_at of this FormResponse.


        :param created_at: The created_at of this FormResponse.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def last_modify(self) -> str:
        """Gets the last_modify of this FormResponse.


        :return: The last_modify of this FormResponse.
        :rtype: str
        """
        return self._last_modify

    @last_modify.setter
    def last_modify(self, last_modify: str):
        """Sets the last_modify of this FormResponse.


        :param last_modify: The last_modify of this FormResponse.
        :type last_modify: str
        """

        self._last_modify = last_modify

    @property
    def answers(self) -> List[Answer]:
        """Gets the answers of this FormResponse.


        :return: The answers of this FormResponse.
        :rtype: List[Answer]
        """
        return self._answers

    @answers.setter
    def answers(self, answers: List[Answer]):
        """Sets the answers of this FormResponse.


        :param answers: The answers of this FormResponse.
        :type answers: List[Answer]
        """

        self._answers = answers
