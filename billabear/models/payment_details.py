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

class PaymentDetails(object):
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
        'id': 'str',
        'name': 'str',
        'default': 'bool',
        'brand': 'str',
        'last_four': 'str',
        'expiry_month': 'str',
        'expiry_year': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'default': 'default',
        'brand': 'brand',
        'last_four': 'last_four',
        'expiry_month': 'expiry_month',
        'expiry_year': 'expiry_year',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, name=None, default=None, brand=None, last_four=None, expiry_month=None, expiry_year=None, created_at=None):  # noqa: E501
        """PaymentDetails - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._default = None
        self._brand = None
        self._last_four = None
        self._expiry_month = None
        self._expiry_year = None
        self._created_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if default is not None:
            self.default = default
        if brand is not None:
            self.brand = brand
        if last_four is not None:
            self.last_four = last_four
        if expiry_month is not None:
            self.expiry_month = expiry_month
        if expiry_year is not None:
            self.expiry_year = expiry_year
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this PaymentDetails.  # noqa: E501


        :return: The id of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentDetails.


        :param id: The id of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PaymentDetails.  # noqa: E501


        :return: The name of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentDetails.


        :param name: The name of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def default(self):
        """Gets the default of this PaymentDetails.  # noqa: E501


        :return: The default of this PaymentDetails.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this PaymentDetails.


        :param default: The default of this PaymentDetails.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def brand(self):
        """Gets the brand of this PaymentDetails.  # noqa: E501


        :return: The brand of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this PaymentDetails.


        :param brand: The brand of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def last_four(self):
        """Gets the last_four of this PaymentDetails.  # noqa: E501


        :return: The last_four of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._last_four

    @last_four.setter
    def last_four(self, last_four):
        """Sets the last_four of this PaymentDetails.


        :param last_four: The last_four of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._last_four = last_four

    @property
    def expiry_month(self):
        """Gets the expiry_month of this PaymentDetails.  # noqa: E501


        :return: The expiry_month of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._expiry_month

    @expiry_month.setter
    def expiry_month(self, expiry_month):
        """Sets the expiry_month of this PaymentDetails.


        :param expiry_month: The expiry_month of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._expiry_month = expiry_month

    @property
    def expiry_year(self):
        """Gets the expiry_year of this PaymentDetails.  # noqa: E501


        :return: The expiry_year of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._expiry_year

    @expiry_year.setter
    def expiry_year(self, expiry_year):
        """Sets the expiry_year of this PaymentDetails.


        :param expiry_year: The expiry_year of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._expiry_year = expiry_year

    @property
    def created_at(self):
        """Gets the created_at of this PaymentDetails.  # noqa: E501


        :return: The created_at of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PaymentDetails.


        :param created_at: The created_at of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

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
        if issubclass(PaymentDetails, dict):
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
        if not isinstance(other, PaymentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
