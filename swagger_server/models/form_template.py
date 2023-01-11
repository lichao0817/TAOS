# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.question import Question  # noqa: F401,E501
from swagger_server import util


class FormTemplate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, owner_id: int=None, created_at: str=None, last_modify: str=None, title: str=None, description: str=None, questions: List[Question]=None):  # noqa: E501
        """FormTemplate - a model defined in Swagger

        :param id: The id of this FormTemplate.  # noqa: E501
        :type id: int
        :param owner_id: The owner_id of this FormTemplate.  # noqa: E501
        :type owner_id: int
        :param created_at: The created_at of this FormTemplate.  # noqa: E501
        :type created_at: str
        :param last_modify: The last_modify of this FormTemplate.  # noqa: E501
        :type last_modify: str
        :param title: The title of this FormTemplate.  # noqa: E501
        :type title: str
        :param description: The description of this FormTemplate.  # noqa: E501
        :type description: str
        :param questions: The questions of this FormTemplate.  # noqa: E501
        :type questions: List[Question]
        """
        self.swagger_types = {
            'id': int,
            'owner_id': int,
            'created_at': str,
            'last_modify': str,
            'title': str,
            'description': str,
            'questions': List[Question]
        }

        self.attribute_map = {
            'id': 'id',
            'owner_id': 'ownerId',
            'created_at': 'createdAt',
            'last_modify': 'lastModify',
            'title': 'title',
            'description': 'description',
            'questions': 'questions'
        }
        self._id = id
        self._owner_id = owner_id
        self._created_at = created_at
        self._last_modify = last_modify
        self._title = title
        self._description = description
        self._questions = questions

    @classmethod
    def from_dict(cls, dikt) -> 'FormTemplate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FormTemplate of this FormTemplate.  # noqa: E501
        :rtype: FormTemplate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this FormTemplate.


        :return: The id of this FormTemplate.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this FormTemplate.


        :param id: The id of this FormTemplate.
        :type id: int
        """

        self._id = id

    @property
    def owner_id(self) -> int:
        """Gets the owner_id of this FormTemplate.


        :return: The owner_id of this FormTemplate.
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: int):
        """Sets the owner_id of this FormTemplate.


        :param owner_id: The owner_id of this FormTemplate.
        :type owner_id: int
        """

        self._owner_id = owner_id

    @property
    def created_at(self) -> str:
        """Gets the created_at of this FormTemplate.


        :return: The created_at of this FormTemplate.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        """Sets the created_at of this FormTemplate.


        :param created_at: The created_at of this FormTemplate.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def last_modify(self) -> str:
        """Gets the last_modify of this FormTemplate.


        :return: The last_modify of this FormTemplate.
        :rtype: str
        """
        return self._last_modify

    @last_modify.setter
    def last_modify(self, last_modify: str):
        """Sets the last_modify of this FormTemplate.


        :param last_modify: The last_modify of this FormTemplate.
        :type last_modify: str
        """

        self._last_modify = last_modify

    @property
    def title(self) -> str:
        """Gets the title of this FormTemplate.


        :return: The title of this FormTemplate.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this FormTemplate.


        :param title: The title of this FormTemplate.
        :type title: str
        """

        self._title = title

    @property
    def description(self) -> str:
        """Gets the description of this FormTemplate.


        :return: The description of this FormTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this FormTemplate.


        :param description: The description of this FormTemplate.
        :type description: str
        """

        self._description = description

    @property
    def questions(self) -> List[Question]:
        """Gets the questions of this FormTemplate.


        :return: The questions of this FormTemplate.
        :rtype: List[Question]
        """
        return self._questions

    @questions.setter
    def questions(self, questions: List[Question]):
        """Sets the questions of this FormTemplate.


        :param questions: The questions of this FormTemplate.
        :type questions: List[Question]
        """

        self._questions = questions
