# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class NotificationDefaults(object):
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
        'api_email_notifications': 'NotificationDefaultSettings',
        'email_notifications': 'NotificationDefaultSettings'
    }

    attribute_map = {
        'api_email_notifications': 'apiEmailNotifications',
        'email_notifications': 'emailNotifications'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """NotificationDefaults - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_email_notifications = None
        self._email_notifications = None
        self.discriminator = None

        setattr(self, "_{}".format('api_email_notifications'), kwargs.get('api_email_notifications', None))
        setattr(self, "_{}".format('email_notifications'), kwargs.get('email_notifications', None))

    @property
    def api_email_notifications(self):
        """Gets the api_email_notifications of this NotificationDefaults.  # noqa: E501


        :return: The api_email_notifications of this NotificationDefaults.  # noqa: E501
        :rtype: NotificationDefaultSettings
        """
        return self._api_email_notifications

    @api_email_notifications.setter
    def api_email_notifications(self, api_email_notifications):
        """Sets the api_email_notifications of this NotificationDefaults.


        :param api_email_notifications: The api_email_notifications of this NotificationDefaults.  # noqa: E501
        :type: NotificationDefaultSettings
        """

        self._api_email_notifications = api_email_notifications

    @property
    def email_notifications(self):
        """Gets the email_notifications of this NotificationDefaults.  # noqa: E501


        :return: The email_notifications of this NotificationDefaults.  # noqa: E501
        :rtype: NotificationDefaultSettings
        """
        return self._email_notifications

    @email_notifications.setter
    def email_notifications(self, email_notifications):
        """Sets the email_notifications of this NotificationDefaults.


        :param email_notifications: The email_notifications of this NotificationDefaults.  # noqa: E501
        :type: NotificationDefaultSettings
        """

        self._email_notifications = email_notifications

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
        if issubclass(NotificationDefaults, dict):
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
        if not isinstance(other, NotificationDefaults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationDefaults):
            return True

        return self.to_dict() != other.to_dict()