# coding: utf-8

"""
    BillaBear

    The REST API provided by BillaBear  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@billabear.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2008(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data': 'list[Subscription]',
        'has_more': 'bool',
        'last_key': 'str'
    }

    attribute_map = {
        'data': 'data',
        'has_more': 'has_more',
        'last_key': 'last_key'
    }

    def __init__(self, data=None, has_more=None, last_key=None):  # noqa: E501
        """InlineResponse2008 - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._has_more = None
        self._last_key = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if has_more is not None:
            self.has_more = has_more
        if last_key is not None:
            self.last_key = last_key

    @property
    def data(self):
        """Gets the data of this InlineResponse2008.  # noqa: E501


        :return: The data of this InlineResponse2008.  # noqa: E501
        :rtype: list[Subscription]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse2008.


        :param data: The data of this InlineResponse2008.  # noqa: E501
        :type: list[Subscription]
        """

        self._data = data

    @property
    def has_more(self):
        """Gets the has_more of this InlineResponse2008.  # noqa: E501


        :return: The has_more of this InlineResponse2008.  # noqa: E501
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this InlineResponse2008.


        :param has_more: The has_more of this InlineResponse2008.  # noqa: E501
        :type: bool
        """

        self._has_more = has_more

    @property
    def last_key(self):
        """Gets the last_key of this InlineResponse2008.  # noqa: E501


        :return: The last_key of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._last_key

    @last_key.setter
    def last_key(self, last_key):
        """Sets the last_key of this InlineResponse2008.


        :param last_key: The last_key of this InlineResponse2008.  # noqa: E501
        :type: str
        """

        self._last_key = last_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse2008, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2008):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
