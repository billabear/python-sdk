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

class InlineResponse2009Data(object):
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
        'amount': 'int',
        'currency': 'str',
        'external_reference': 'str',
        'status': 'str',
        'created_at': 'str',
        'customer': 'Customer',
        'receipts': 'list[InlineResponse2009Receipts]'
    }

    attribute_map = {
        'id': 'id',
        'amount': 'amount',
        'currency': 'currency',
        'external_reference': 'external_reference',
        'status': 'status',
        'created_at': 'created_at',
        'customer': 'customer',
        'receipts': 'receipts'
    }

    def __init__(self, id=None, amount=None, currency=None, external_reference=None, status=None, created_at=None, customer=None, receipts=None):  # noqa: E501
        """InlineResponse2009Data - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._amount = None
        self._currency = None
        self._external_reference = None
        self._status = None
        self._created_at = None
        self._customer = None
        self._receipts = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if external_reference is not None:
            self.external_reference = external_reference
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if customer is not None:
            self.customer = customer
        if receipts is not None:
            self.receipts = receipts

    @property
    def id(self):
        """Gets the id of this InlineResponse2009Data.  # noqa: E501


        :return: The id of this InlineResponse2009Data.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2009Data.


        :param id: The id of this InlineResponse2009Data.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def amount(self):
        """Gets the amount of this InlineResponse2009Data.  # noqa: E501


        :return: The amount of this InlineResponse2009Data.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse2009Data.


        :param amount: The amount of this InlineResponse2009Data.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this InlineResponse2009Data.  # noqa: E501

        Three-letter ISO currency code. Must be upper-case  # noqa: E501

        :return: The currency of this InlineResponse2009Data.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InlineResponse2009Data.

        Three-letter ISO currency code. Must be upper-case  # noqa: E501

        :param currency: The currency of this InlineResponse2009Data.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def external_reference(self):
        """Gets the external_reference of this InlineResponse2009Data.  # noqa: E501


        :return: The external_reference of this InlineResponse2009Data.  # noqa: E501
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this InlineResponse2009Data.


        :param external_reference: The external_reference of this InlineResponse2009Data.  # noqa: E501
        :type: str
        """

        self._external_reference = external_reference

    @property
    def status(self):
        """Gets the status of this InlineResponse2009Data.  # noqa: E501


        :return: The status of this InlineResponse2009Data.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2009Data.


        :param status: The status of this InlineResponse2009Data.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "completed", "disputed", "partially_refunded", "fully_refunded"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse2009Data.  # noqa: E501


        :return: The created_at of this InlineResponse2009Data.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse2009Data.


        :param created_at: The created_at of this InlineResponse2009Data.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def customer(self):
        """Gets the customer of this InlineResponse2009Data.  # noqa: E501


        :return: The customer of this InlineResponse2009Data.  # noqa: E501
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this InlineResponse2009Data.


        :param customer: The customer of this InlineResponse2009Data.  # noqa: E501
        :type: Customer
        """

        self._customer = customer

    @property
    def receipts(self):
        """Gets the receipts of this InlineResponse2009Data.  # noqa: E501


        :return: The receipts of this InlineResponse2009Data.  # noqa: E501
        :rtype: list[InlineResponse2009Receipts]
        """
        return self._receipts

    @receipts.setter
    def receipts(self, receipts):
        """Sets the receipts of this InlineResponse2009Data.


        :param receipts: The receipts of this InlineResponse2009Data.  # noqa: E501
        :type: list[InlineResponse2009Receipts]
        """

        self._receipts = receipts

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
        if issubclass(InlineResponse2009Data, dict):
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
        if not isinstance(other, InlineResponse2009Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
