# coding: utf-8

"""
    Pulse API

    Integrate all of your testing apps with Pulse API

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse200(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, auth_token=None, user_id=None, account_id=None):
        """
        InlineResponse200 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'auth_token': 'str',
            'user_id': 'str',
            'account_id': 'str'
        }

        self.attribute_map = {
            'auth_token': 'authToken',
            'user_id': 'userId',
            'account_id': 'accountId'
        }

        self._auth_token = auth_token
        self._user_id = user_id
        self._account_id = account_id

    @property
    def auth_token(self):
        """
        Gets the auth_token of this InlineResponse200.

        :return: The auth_token of this InlineResponse200.
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """
        Sets the auth_token of this InlineResponse200.

        :param auth_token: The auth_token of this InlineResponse200.
        :type: str
        """

        self._auth_token = auth_token

    @property
    def user_id(self):
        """
        Gets the user_id of this InlineResponse200.

        :return: The user_id of this InlineResponse200.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this InlineResponse200.

        :param user_id: The user_id of this InlineResponse200.
        :type: str
        """

        self._user_id = user_id

    @property
    def account_id(self):
        """
        Gets the account_id of this InlineResponse200.

        :return: The account_id of this InlineResponse200.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this InlineResponse200.

        :param account_id: The account_id of this InlineResponse200.
        :type: str
        """

        self._account_id = account_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
