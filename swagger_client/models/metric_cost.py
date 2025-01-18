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

class MetricCost(object):
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
        'name': 'str',
        'amount': 'int',
        'currency': 'str',
        'usage': 'float'
    }

    attribute_map = {
        'name': 'name',
        'amount': 'amount',
        'currency': 'currency',
        'usage': 'usage'
    }

    def __init__(self, name=None, amount=None, currency=None, usage=None):  # noqa: E501
        """MetricCost - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._amount = None
        self._currency = None
        self._usage = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if usage is not None:
            self.usage = usage

    @property
    def name(self):
        """Gets the name of this MetricCost.  # noqa: E501

        The name of the metric that the cost is for  # noqa: E501

        :return: The name of this MetricCost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetricCost.

        The name of the metric that the cost is for  # noqa: E501

        :param name: The name of this MetricCost.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def amount(self):
        """Gets the amount of this MetricCost.  # noqa: E501


        :return: The amount of this MetricCost.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this MetricCost.


        :param amount: The amount of this MetricCost.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this MetricCost.  # noqa: E501


        :return: The currency of this MetricCost.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this MetricCost.


        :param currency: The currency of this MetricCost.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def usage(self):
        """Gets the usage of this MetricCost.  # noqa: E501


        :return: The usage of this MetricCost.  # noqa: E501
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this MetricCost.


        :param usage: The usage of this MetricCost.  # noqa: E501
        :type: float
        """

        self._usage = usage

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
        if issubclass(MetricCost, dict):
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
        if not isinstance(other, MetricCost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
