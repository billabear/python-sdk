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

class SubscriptionPlan(object):
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
        'code_name': 'str',
        'user_count': 'int',
        'per_seat': 'bool',
        'has_trial': 'bool',
        'is_trial_standalone': 'bool',
        'free': 'bool',
        'public': 'bool',
        'limits': 'list[Limit]',
        'features': 'list[Feature]',
        'product': 'Product',
        'prices': 'list[Price]',
        'trial_length_days': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'code_name': 'code_name',
        'user_count': 'user_count',
        'per_seat': 'per_seat',
        'has_trial': 'has_trial',
        'is_trial_standalone': 'is_trial_standalone',
        'free': 'free',
        'public': 'public',
        'limits': 'limits',
        'features': 'features',
        'product': 'product',
        'prices': 'prices',
        'trial_length_days': 'trial_length_days'
    }

    def __init__(self, id=None, name=None, code_name=None, user_count=None, per_seat=None, has_trial=None, is_trial_standalone=None, free=None, public=None, limits=None, features=None, product=None, prices=None, trial_length_days=None):  # noqa: E501
        """SubscriptionPlan - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._code_name = None
        self._user_count = None
        self._per_seat = None
        self._has_trial = None
        self._is_trial_standalone = None
        self._free = None
        self._public = None
        self._limits = None
        self._features = None
        self._product = None
        self._prices = None
        self._trial_length_days = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if code_name is not None:
            self.code_name = code_name
        if user_count is not None:
            self.user_count = user_count
        if per_seat is not None:
            self.per_seat = per_seat
        if has_trial is not None:
            self.has_trial = has_trial
        if is_trial_standalone is not None:
            self.is_trial_standalone = is_trial_standalone
        if free is not None:
            self.free = free
        if public is not None:
            self.public = public
        if limits is not None:
            self.limits = limits
        if features is not None:
            self.features = features
        if product is not None:
            self.product = product
        if prices is not None:
            self.prices = prices
        if trial_length_days is not None:
            self.trial_length_days = trial_length_days

    @property
    def id(self):
        """Gets the id of this SubscriptionPlan.  # noqa: E501


        :return: The id of this SubscriptionPlan.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionPlan.


        :param id: The id of this SubscriptionPlan.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SubscriptionPlan.  # noqa: E501


        :return: The name of this SubscriptionPlan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionPlan.


        :param name: The name of this SubscriptionPlan.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def code_name(self):
        """Gets the code_name of this SubscriptionPlan.  # noqa: E501


        :return: The code_name of this SubscriptionPlan.  # noqa: E501
        :rtype: str
        """
        return self._code_name

    @code_name.setter
    def code_name(self, code_name):
        """Sets the code_name of this SubscriptionPlan.


        :param code_name: The code_name of this SubscriptionPlan.  # noqa: E501
        :type: str
        """

        self._code_name = code_name

    @property
    def user_count(self):
        """Gets the user_count of this SubscriptionPlan.  # noqa: E501


        :return: The user_count of this SubscriptionPlan.  # noqa: E501
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this SubscriptionPlan.


        :param user_count: The user_count of this SubscriptionPlan.  # noqa: E501
        :type: int
        """

        self._user_count = user_count

    @property
    def per_seat(self):
        """Gets the per_seat of this SubscriptionPlan.  # noqa: E501


        :return: The per_seat of this SubscriptionPlan.  # noqa: E501
        :rtype: bool
        """
        return self._per_seat

    @per_seat.setter
    def per_seat(self, per_seat):
        """Sets the per_seat of this SubscriptionPlan.


        :param per_seat: The per_seat of this SubscriptionPlan.  # noqa: E501
        :type: bool
        """

        self._per_seat = per_seat

    @property
    def has_trial(self):
        """Gets the has_trial of this SubscriptionPlan.  # noqa: E501


        :return: The has_trial of this SubscriptionPlan.  # noqa: E501
        :rtype: bool
        """
        return self._has_trial

    @has_trial.setter
    def has_trial(self, has_trial):
        """Sets the has_trial of this SubscriptionPlan.


        :param has_trial: The has_trial of this SubscriptionPlan.  # noqa: E501
        :type: bool
        """

        self._has_trial = has_trial

    @property
    def is_trial_standalone(self):
        """Gets the is_trial_standalone of this SubscriptionPlan.  # noqa: E501


        :return: The is_trial_standalone of this SubscriptionPlan.  # noqa: E501
        :rtype: bool
        """
        return self._is_trial_standalone

    @is_trial_standalone.setter
    def is_trial_standalone(self, is_trial_standalone):
        """Sets the is_trial_standalone of this SubscriptionPlan.


        :param is_trial_standalone: The is_trial_standalone of this SubscriptionPlan.  # noqa: E501
        :type: bool
        """

        self._is_trial_standalone = is_trial_standalone

    @property
    def free(self):
        """Gets the free of this SubscriptionPlan.  # noqa: E501


        :return: The free of this SubscriptionPlan.  # noqa: E501
        :rtype: bool
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this SubscriptionPlan.


        :param free: The free of this SubscriptionPlan.  # noqa: E501
        :type: bool
        """

        self._free = free

    @property
    def public(self):
        """Gets the public of this SubscriptionPlan.  # noqa: E501


        :return: The public of this SubscriptionPlan.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this SubscriptionPlan.


        :param public: The public of this SubscriptionPlan.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def limits(self):
        """Gets the limits of this SubscriptionPlan.  # noqa: E501


        :return: The limits of this SubscriptionPlan.  # noqa: E501
        :rtype: list[Limit]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this SubscriptionPlan.


        :param limits: The limits of this SubscriptionPlan.  # noqa: E501
        :type: list[Limit]
        """

        self._limits = limits

    @property
    def features(self):
        """Gets the features of this SubscriptionPlan.  # noqa: E501


        :return: The features of this SubscriptionPlan.  # noqa: E501
        :rtype: list[Feature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this SubscriptionPlan.


        :param features: The features of this SubscriptionPlan.  # noqa: E501
        :type: list[Feature]
        """

        self._features = features

    @property
    def product(self):
        """Gets the product of this SubscriptionPlan.  # noqa: E501


        :return: The product of this SubscriptionPlan.  # noqa: E501
        :rtype: Product
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this SubscriptionPlan.


        :param product: The product of this SubscriptionPlan.  # noqa: E501
        :type: Product
        """

        self._product = product

    @property
    def prices(self):
        """Gets the prices of this SubscriptionPlan.  # noqa: E501


        :return: The prices of this SubscriptionPlan.  # noqa: E501
        :rtype: list[Price]
        """
        return self._prices

    @prices.setter
    def prices(self, prices):
        """Sets the prices of this SubscriptionPlan.


        :param prices: The prices of this SubscriptionPlan.  # noqa: E501
        :type: list[Price]
        """

        self._prices = prices

    @property
    def trial_length_days(self):
        """Gets the trial_length_days of this SubscriptionPlan.  # noqa: E501


        :return: The trial_length_days of this SubscriptionPlan.  # noqa: E501
        :rtype: int
        """
        return self._trial_length_days

    @trial_length_days.setter
    def trial_length_days(self, trial_length_days):
        """Sets the trial_length_days of this SubscriptionPlan.


        :param trial_length_days: The trial_length_days of this SubscriptionPlan.  # noqa: E501
        :type: int
        """

        self._trial_length_days = trial_length_days

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
        if issubclass(SubscriptionPlan, dict):
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
        if not isinstance(other, SubscriptionPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
