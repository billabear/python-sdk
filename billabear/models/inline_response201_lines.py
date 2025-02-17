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

class InlineResponse201Lines(object):
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
        'subscription_plan': 'SubscriptionPlan',
        'price': 'Price',
        'description': 'str',
        'currency': 'str',
        'seat_number': 'int',
        'sub_total': 'int',
        'tax_total': 'int',
        'tax_rate': 'float'
    }

    attribute_map = {
        'subscription_plan': 'subscription_plan',
        'price': 'price',
        'description': 'description',
        'currency': 'currency',
        'seat_number': 'seat_number',
        'sub_total': 'sub_total',
        'tax_total': 'tax_total',
        'tax_rate': 'tax_rate'
    }

    def __init__(self, subscription_plan=None, price=None, description=None, currency=None, seat_number=None, sub_total=None, tax_total=None, tax_rate=None):  # noqa: E501
        """InlineResponse201Lines - a model defined in Swagger"""  # noqa: E501
        self._subscription_plan = None
        self._price = None
        self._description = None
        self._currency = None
        self._seat_number = None
        self._sub_total = None
        self._tax_total = None
        self._tax_rate = None
        self.discriminator = None
        if subscription_plan is not None:
            self.subscription_plan = subscription_plan
        if price is not None:
            self.price = price
        if description is not None:
            self.description = description
        if currency is not None:
            self.currency = currency
        if seat_number is not None:
            self.seat_number = seat_number
        if sub_total is not None:
            self.sub_total = sub_total
        if tax_total is not None:
            self.tax_total = tax_total
        if tax_rate is not None:
            self.tax_rate = tax_rate

    @property
    def subscription_plan(self):
        """Gets the subscription_plan of this InlineResponse201Lines.  # noqa: E501


        :return: The subscription_plan of this InlineResponse201Lines.  # noqa: E501
        :rtype: SubscriptionPlan
        """
        return self._subscription_plan

    @subscription_plan.setter
    def subscription_plan(self, subscription_plan):
        """Sets the subscription_plan of this InlineResponse201Lines.


        :param subscription_plan: The subscription_plan of this InlineResponse201Lines.  # noqa: E501
        :type: SubscriptionPlan
        """

        self._subscription_plan = subscription_plan

    @property
    def price(self):
        """Gets the price of this InlineResponse201Lines.  # noqa: E501


        :return: The price of this InlineResponse201Lines.  # noqa: E501
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this InlineResponse201Lines.


        :param price: The price of this InlineResponse201Lines.  # noqa: E501
        :type: Price
        """

        self._price = price

    @property
    def description(self):
        """Gets the description of this InlineResponse201Lines.  # noqa: E501


        :return: The description of this InlineResponse201Lines.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse201Lines.


        :param description: The description of this InlineResponse201Lines.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def currency(self):
        """Gets the currency of this InlineResponse201Lines.  # noqa: E501


        :return: The currency of this InlineResponse201Lines.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InlineResponse201Lines.


        :param currency: The currency of this InlineResponse201Lines.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def seat_number(self):
        """Gets the seat_number of this InlineResponse201Lines.  # noqa: E501


        :return: The seat_number of this InlineResponse201Lines.  # noqa: E501
        :rtype: int
        """
        return self._seat_number

    @seat_number.setter
    def seat_number(self, seat_number):
        """Sets the seat_number of this InlineResponse201Lines.


        :param seat_number: The seat_number of this InlineResponse201Lines.  # noqa: E501
        :type: int
        """

        self._seat_number = seat_number

    @property
    def sub_total(self):
        """Gets the sub_total of this InlineResponse201Lines.  # noqa: E501


        :return: The sub_total of this InlineResponse201Lines.  # noqa: E501
        :rtype: int
        """
        return self._sub_total

    @sub_total.setter
    def sub_total(self, sub_total):
        """Sets the sub_total of this InlineResponse201Lines.


        :param sub_total: The sub_total of this InlineResponse201Lines.  # noqa: E501
        :type: int
        """

        self._sub_total = sub_total

    @property
    def tax_total(self):
        """Gets the tax_total of this InlineResponse201Lines.  # noqa: E501


        :return: The tax_total of this InlineResponse201Lines.  # noqa: E501
        :rtype: int
        """
        return self._tax_total

    @tax_total.setter
    def tax_total(self, tax_total):
        """Sets the tax_total of this InlineResponse201Lines.


        :param tax_total: The tax_total of this InlineResponse201Lines.  # noqa: E501
        :type: int
        """

        self._tax_total = tax_total

    @property
    def tax_rate(self):
        """Gets the tax_rate of this InlineResponse201Lines.  # noqa: E501


        :return: The tax_rate of this InlineResponse201Lines.  # noqa: E501
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this InlineResponse201Lines.


        :param tax_rate: The tax_rate of this InlineResponse201Lines.  # noqa: E501
        :type: float
        """

        self._tax_rate = tax_rate

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
        if issubclass(InlineResponse201Lines, dict):
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
        if not isinstance(other, InlineResponse201Lines):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
