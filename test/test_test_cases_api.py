# coding: utf-8

"""
    Pulse API

    Integrate all of your testing apps with Pulse API

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.test_cases_api import TestCasesApi


class TestTestCasesApi(unittest.TestCase):
    """ TestCasesApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.test_cases_api.TestCasesApi()

    def tearDown(self):
        pass

    def test_create_test_case(self):
        """
        Test case for create_test_case

        createTestCase
        """
        pass

    def test_delete_test_case(self):
        """
        Test case for delete_test_case

        deleteTestCase
        """
        pass

    def test_get_all_test_cases(self):
        """
        Test case for get_all_test_cases

        getTestCases
        """
        pass

    def test_get_test_case(self):
        """
        Test case for get_test_case

        getTestCase
        """
        pass

    def test_update_test_case(self):
        """
        Test case for update_test_case

        updateTestCase
        """
        pass


if __name__ == '__main__':
    unittest.main()
