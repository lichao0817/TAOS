# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class FormAssignment(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, owner_id: int=None, client_id: int=None, template_id: int=None, response_id: int=None, created_at: str=None, last_modify: str=None, status: str=None):  # noqa: E501
        """FormAssignment - a model defined in Swagger

        :param id: The id of this FormAssignment.  # noqa: E501
        :type id: int
        :param owner_id: The owner_id of this FormAssignment.  # noqa: E501
        :type owner_id: int
        :param client_id: The client_id of this FormAssignment.  # noqa: E501
        :type client_id: int
        :param template_id: The template_id of this FormAssignment.  # noqa: E501
        :type template_id: int
        :param response_id: The response_id of this FormAssignment.  # noqa: E501
        :type response_id: int
        :param created_at: The created_at of this FormAssignment.  # noqa: E501
        :type created_at: str
        :param last_modify: The last_modify of this FormAssignment.  # noqa: E501
        :type last_modify: str
        :param status: The status of this FormAssignment.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'id': int,
            'owner_id': int,
            'client_id': int,
            'template_id': int,
            'response_id': int,
            'created_at': str,
            'last_modify': str,
            'status': str
        }

        self.attribute_map = {
            'id': 'id',
            'owner_id': 'ownerId',
            'client_id': 'clientId',
            'template_id': 'templateId',
            'response_id': 'responseId',
            'created_at': 'createdAt',
            'last_modify': 'lastModify',
            'status': 'status'
        }
        self._id = id
        self._owner_id = owner_id
        self._client_id = client_id
        self._template_id = template_id
        self._response_id = response_id
        self._created_at = created_at
        self._last_modify = last_modify
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'FormAssignment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FormAssignment of this FormAssignment.  # noqa: E501
        :rtype: FormAssignment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this FormAssignment.


        :return: The id of this FormAssignment.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this FormAssignment.


        :param id: The id of this FormAssignment.
        :type id: int
        """

        self._id = id

    @property
    def owner_id(self) -> int:
        """Gets the owner_id of this FormAssignment.


        :return: The owner_id of this FormAssignment.
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: int):
        """Sets the owner_id of this FormAssignment.


        :param owner_id: The owner_id of this FormAssignment.
        :type owner_id: int
        """

        self._owner_id = owner_id

    @property
    def client_id(self) -> int:
        """Gets the client_id of this FormAssignment.


        :return: The client_id of this FormAssignment.
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: int):
        """Sets the client_id of this FormAssignment.


        :param client_id: The client_id of this FormAssignment.
        :type client_id: int
        """

        self._client_id = client_id

    @property
    def template_id(self) -> int:
        """Gets the template_id of this FormAssignment.


        :return: The template_id of this FormAssignment.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id: int):
        """Sets the template_id of this FormAssignment.


        :param template_id: The template_id of this FormAssignment.
        :type template_id: int
        """

        self._template_id = template_id

    @property
    def response_id(self) -> int:
        """Gets the response_id of this FormAssignment.


        :return: The response_id of this FormAssignment.
        :rtype: int
        """
        return self._response_id

    @response_id.setter
    def response_id(self, response_id: int):
        """Sets the response_id of this FormAssignment.


        :param response_id: The response_id of this FormAssignment.
        :type response_id: int
        """

        self._response_id = response_id

    @property
    def created_at(self) -> str:
        """Gets the created_at of this FormAssignment.


        :return: The created_at of this FormAssignment.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        """Sets the created_at of this FormAssignment.


        :param created_at: The created_at of this FormAssignment.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def last_modify(self) -> str:
        """Gets the last_modify of this FormAssignment.


        :return: The last_modify of this FormAssignment.
        :rtype: str
        """
        return self._last_modify

    @last_modify.setter
    def last_modify(self, last_modify: str):
        """Sets the last_modify of this FormAssignment.


        :param last_modify: The last_modify of this FormAssignment.
        :type last_modify: str
        """

        self._last_modify = last_modify

    @property
    def status(self) -> str:
        """Gets the status of this FormAssignment.


        :return: The status of this FormAssignment.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this FormAssignment.


        :param status: The status of this FormAssignment.
        :type status: str
        """
        allowed_values = ["open", "complete"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
