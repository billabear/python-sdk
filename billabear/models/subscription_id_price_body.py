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

class SubscriptionIdPriceBody(object):
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
        'price': 'Uuid',
        'when': 'str'
    }

    attribute_map = {
        'price': 'price',
        'when': 'when'
    }

    def __init__(self, price=None, when=None):  # noqa: E501
        """SubscriptionIdPriceBody - a model defined in Swagger"""  # noqa: E501
        self._price = None
        self._when = None
        self.discriminator = None
        self.price = price
        self.when = when

    @property
    def price(self):
        """Gets the price of this SubscriptionIdPriceBody.  # noqa: E501


        :return: The price of this SubscriptionIdPriceBody.  # noqa: E501
        :rtype: Uuid
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SubscriptionIdPriceBody.


        :param price: The price of this SubscriptionIdPriceBody.  # noqa: E501
        :type: Uuid
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def when(self):
        """Gets the when of this SubscriptionIdPriceBody.  # noqa: E501


        :return: The when of this SubscriptionIdPriceBody.  # noqa: E501
        :rtype: str
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this SubscriptionIdPriceBody.


        :param when: The when of this SubscriptionIdPriceBody.  # noqa: E501
        :type: str
        """
        if when is None:
            raise ValueError("Invalid value for `when`, must not be `None`")  # noqa: E501
        allowed_values = ["next_cycle", "instantly"]  # noqa: E501
        if when not in allowed_values:
            raise ValueError(
                "Invalid value for `when` ({0}), must be one of {1}"  # noqa: E501
                .format(when, allowed_values)
            )

        self._when = when

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
        if issubclass(SubscriptionIdPriceBody, dict):
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
        if not isinstance(other, SubscriptionIdPriceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
