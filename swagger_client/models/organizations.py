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


class Organizations(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, members=None, account_id=None):
        """
        Organizations - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'members': 'list[OrganizationMemberSchema]',
            'account_id': 'str'
        }

        self.attribute_map = {
            'id': '_id',
            'name': 'name',
            'members': 'members',
            'account_id': 'accountId'
        }

        self._id = id
        self._name = name
        self._members = members
        self._account_id = account_id

    @property
    def id(self):
        """
        Gets the id of this Organizations.
        _id of the Organizations.

        :return: The id of this Organizations.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Organizations.
        _id of the Organizations.

        :param id: The id of this Organizations.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Organizations.
        name of the Organizations.

        :return: The name of this Organizations.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Organizations.
        name of the Organizations.

        :param name: The name of this Organizations.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def members(self):
        """
        Gets the members of this Organizations.
        members of the Organizations.

        :return: The members of this Organizations.
        :rtype: list[OrganizationMemberSchema]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this Organizations.
        members of the Organizations.

        :param members: The members of this Organizations.
        :type: list[OrganizationMemberSchema]
        """
        if members is None:
            raise ValueError("Invalid value for `members`, must not be `None`")

        self._members = members

    @property
    def account_id(self):
        """
        Gets the account_id of this Organizations.
        accountId of the Organizations.

        :return: The account_id of this Organizations.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this Organizations.
        accountId of the Organizations.

        :param account_id: The account_id of this Organizations.
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")

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