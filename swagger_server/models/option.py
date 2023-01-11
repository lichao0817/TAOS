# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Option(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, option_index: str=None, question_id: int=None, created_at: str=None, last_modify: str=None, description: str=None):  # noqa: E501
        """Option - a model defined in Swagger

        :param id: The id of this Option.  # noqa: E501
        :type id: int
        :param option_index: The option_index of this Option.  # noqa: E501
        :type option_index: str
        :param question_id: The question_id of this Option.  # noqa: E501
        :type question_id: int
        :param created_at: The created_at of this Option.  # noqa: E501
        :type created_at: str
        :param last_modify: The last_modify of this Option.  # noqa: E501
        :type last_modify: str
        :param description: The description of this Option.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'id': int,
            'option_index': str,
            'question_id': int,
            'created_at': str,
            'last_modify': str,
            'description': str
        }

        self.attribute_map = {
            'id': 'id',
            'option_index': 'optionIndex',
            'question_id': 'questionId',
            'created_at': 'createdAt',
            'last_modify': 'lastModify',
            'description': 'description'
        }
        self._id = id
        self._option_index = option_index
        self._question_id = question_id
        self._created_at = created_at
        self._last_modify = last_modify
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'Option':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Option of this Option.  # noqa: E501
        :rtype: Option
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Option.


        :return: The id of this Option.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Option.


        :param id: The id of this Option.
        :type id: int
        """

        self._id = id

    @property
    def option_index(self) -> str:
        """Gets the option_index of this Option.


        :return: The option_index of this Option.
        :rtype: str
        """
        return self._option_index

    @option_index.setter
    def option_index(self, option_index: str):
        """Sets the option_index of this Option.


        :param option_index: The option_index of this Option.
        :type option_index: str
        """

        self._option_index = option_index

    @property
    def question_id(self) -> int:
        """Gets the question_id of this Option.


        :return: The question_id of this Option.
        :rtype: int
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id: int):
        """Sets the question_id of this Option.


        :param question_id: The question_id of this Option.
        :type question_id: int
        """

        self._question_id = question_id

    @property
    def created_at(self) -> str:
        """Gets the created_at of this Option.


        :return: The created_at of this Option.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        """Sets the created_at of this Option.


        :param created_at: The created_at of this Option.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def last_modify(self) -> str:
        """Gets the last_modify of this Option.


        :return: The last_modify of this Option.
        :rtype: str
        """
        return self._last_modify

    @last_modify.setter
    def last_modify(self, last_modify: str):
        """Sets the last_modify of this Option.


        :param last_modify: The last_modify of this Option.
        :type last_modify: str
        """

        self._last_modify = last_modify

    @property
    def description(self) -> str:
        """Gets the description of this Option.


        :return: The description of this Option.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Option.


        :param description: The description of this Option.
        :type description: str
        """

        self._description = description
