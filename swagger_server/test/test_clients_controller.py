# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.form_assignment import FormAssignment  # noqa: E501
from swagger_server.models.form_response import FormResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClientsController(BaseTestCase):
    """ClientsController integration test stubs"""

    def test_complete_form_for_client(self):
        """Test case for complete_form_for_client

        Complete the form with formId
        """
        body = FormResponse()
        response = self.client.open(
            '/lichao0817/TAOS/1.0.0/clients/{clientId}/forms/{formId}'.format(client_id=56, form_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_form_response_for_client(self):
        """Test case for find_form_response_for_client

        Find the completed response of the form with formId for a client
        """
        response = self.client.open(
            '/lichao0817/TAOS/1.0.0/clients/{clientId}/forms/{formId}'.format(client_id=56, form_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_forms_for_client(self):
        """Test case for get_all_forms_for_client

        Find all forms assignments for a client
        """
        response = self.client.open(
            '/lichao0817/TAOS/1.0.0/clients/{clientId}/forms'.format(client_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
