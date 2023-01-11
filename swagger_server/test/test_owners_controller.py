# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.form_template import FormTemplate  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOwnersController(BaseTestCase):
    """OwnersController integration test stubs"""

    def test_add_form(self):
        """Test case for add_form

        Add a form for owner
        """
        body = FormTemplate()
        response = self.client.open(
            '/lichao0817/TAOS/1.0.0/owners/{userId}/templates'.format(user_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_clients_for_owner(self):
        """Test case for find_all_clients_for_owner

        Find all clients for an owner
        """
        response = self.client.open(
            '/lichao0817/TAOS/1.0.0/owners/{ownerId}/clients'.format(owner_id=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_forms_for_owner(self):
        """Test case for get_all_forms_for_owner

        Find all form templates for an owner
        """
        response = self.client.open(
            '/lichao0817/TAOS/1.0.0/owners/{userId}/templates'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_form_for_owner(self):
        """Test case for get_form_for_owner

        Find the form with formId for an owner
        """
        response = self.client.open(
            '/lichao0817/TAOS/1.0.0/owners/{userId}/templates/{templateId}'.format(user_id=56, template_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
