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

class Event(object):
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
        'event_id': 'str',
        'subscription': 'str',
        'properties': 'object',
        'value': 'float',
        'code': 'str'
    }

    attribute_map = {
        'event_id': 'event_id',
        'subscription': 'subscription',
        'properties': 'properties',
        'value': 'value',
        'code': 'code'
    }

    def __init__(self, event_id=None, subscription=None, properties=None, value=None, code=None):  # noqa: E501
        """Event - a model defined in Swagger"""  # noqa: E501
        self._event_id = None
        self._subscription = None
        self._properties = None
        self._value = None
        self._code = None
        self.discriminator = None
        self.event_id = event_id
        self.subscription = subscription
        if properties is not None:
            self.properties = properties
        self.value = value
        self.code = code

    @property
    def event_id(self):
        """Gets the event_id of this Event.  # noqa: E501


        :return: The event_id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this Event.


        :param event_id: The event_id of this Event.  # noqa: E501
        :type: str
        """
        if event_id is None:
            raise ValueError("Invalid value for `event_id`, must not be `None`")  # noqa: E501

        self._event_id = event_id

    @property
    def subscription(self):
        """Gets the subscription of this Event.  # noqa: E501


        :return: The subscription of this Event.  # noqa: E501
        :rtype: str
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this Event.


        :param subscription: The subscription of this Event.  # noqa: E501
        :type: str
        """
        if subscription is None:
            raise ValueError("Invalid value for `subscription`, must not be `None`")  # noqa: E501

        self._subscription = subscription

    @property
    def properties(self):
        """Gets the properties of this Event.  # noqa: E501


        :return: The properties of this Event.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Event.


        :param properties: The properties of this Event.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def value(self):
        """Gets the value of this Event.  # noqa: E501


        :return: The value of this Event.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Event.


        :param value: The value of this Event.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def code(self):
        """Gets the code of this Event.  # noqa: E501


        :return: The code of this Event.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Event.


        :param code: The code of this Event.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

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
        if issubclass(Event, dict):
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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
