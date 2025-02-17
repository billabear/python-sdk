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

class CheckoutBody(object):
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
        'brand': 'str',
        'slug': 'str',
        'customer': 'str',
        'items': 'list[CheckoutItems]',
        'subscriptions': 'list[CheckoutSubscriptions]'
    }

    attribute_map = {
        'name': 'name',
        'brand': 'brand',
        'slug': 'slug',
        'customer': 'customer',
        'items': 'items',
        'subscriptions': 'subscriptions'
    }

    def __init__(self, name=None, brand=None, slug=None, customer=None, items=None, subscriptions=None):  # noqa: E501
        """CheckoutBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._brand = None
        self._slug = None
        self._customer = None
        self._items = None
        self._subscriptions = None
        self.discriminator = None
        if name is not None:
            self.name = name
        self.brand = brand
        if slug is not None:
            self.slug = slug
        self.customer = customer
        if items is not None:
            self.items = items
        if subscriptions is not None:
            self.subscriptions = subscriptions

    @property
    def name(self):
        """Gets the name of this CheckoutBody.  # noqa: E501


        :return: The name of this CheckoutBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CheckoutBody.


        :param name: The name of this CheckoutBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def brand(self):
        """Gets the brand of this CheckoutBody.  # noqa: E501


        :return: The brand of this CheckoutBody.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this CheckoutBody.


        :param brand: The brand of this CheckoutBody.  # noqa: E501
        :type: str
        """
        if brand is None:
            raise ValueError("Invalid value for `brand`, must not be `None`")  # noqa: E501

        self._brand = brand

    @property
    def slug(self):
        """Gets the slug of this CheckoutBody.  # noqa: E501


        :return: The slug of this CheckoutBody.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this CheckoutBody.


        :param slug: The slug of this CheckoutBody.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def customer(self):
        """Gets the customer of this CheckoutBody.  # noqa: E501


        :return: The customer of this CheckoutBody.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this CheckoutBody.


        :param customer: The customer of this CheckoutBody.  # noqa: E501
        :type: str
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def items(self):
        """Gets the items of this CheckoutBody.  # noqa: E501


        :return: The items of this CheckoutBody.  # noqa: E501
        :rtype: list[CheckoutItems]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CheckoutBody.


        :param items: The items of this CheckoutBody.  # noqa: E501
        :type: list[CheckoutItems]
        """

        self._items = items

    @property
    def subscriptions(self):
        """Gets the subscriptions of this CheckoutBody.  # noqa: E501


        :return: The subscriptions of this CheckoutBody.  # noqa: E501
        :rtype: list[CheckoutSubscriptions]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this CheckoutBody.


        :param subscriptions: The subscriptions of this CheckoutBody.  # noqa: E501
        :type: list[CheckoutSubscriptions]
        """

        self._subscriptions = subscriptions

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
        if issubclass(CheckoutBody, dict):
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
        if not isinstance(other, CheckoutBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
