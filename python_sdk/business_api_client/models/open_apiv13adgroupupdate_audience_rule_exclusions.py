# coding: utf-8

"""
 Copyright 2023 TikTok Pte. Ltd.

 This source code is licensed under the MIT license found in
 the LICENSE file in the root directory of this source tree.
"""
import pprint
import re  # noqa: F401

import six

class OpenApiv13adgroupupdateAudienceRuleExclusions(object):
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
        'operator': 'str',
        'rules': 'list[OpenApiv13adgroupcreateAudienceRuleInclusionsRules]'
    }

    attribute_map = {
        'operator': 'operator',
        'rules': 'rules'
    }

    def __init__(self, operator=None, rules=None):  # noqa: E501
        """OpenApiv13adgroupupdateAudienceRuleExclusions - a model defined in Swagger"""  # noqa: E501
        self._operator = None
        self._rules = None
        self.discriminator = None
        if operator is not None:
            self.operator = operator
        if rules is not None:
            self.rules = rules

    @property
    def operator(self):
        """Gets the operator of this OpenApiv13adgroupupdateAudienceRuleExclusions.  # noqa: E501


        :return: The operator of this OpenApiv13adgroupupdateAudienceRuleExclusions.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this OpenApiv13adgroupupdateAudienceRuleExclusions.


        :param operator: The operator of this OpenApiv13adgroupupdateAudienceRuleExclusions.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def rules(self):
        """Gets the rules of this OpenApiv13adgroupupdateAudienceRuleExclusions.  # noqa: E501


        :return: The rules of this OpenApiv13adgroupupdateAudienceRuleExclusions.  # noqa: E501
        :rtype: list[OpenApiv13adgroupcreateAudienceRuleInclusionsRules]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this OpenApiv13adgroupupdateAudienceRuleExclusions.


        :param rules: The rules of this OpenApiv13adgroupupdateAudienceRuleExclusions.  # noqa: E501
        :type: list[OpenApiv13adgroupcreateAudienceRuleInclusionsRules]
        """

        self._rules = rules

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
        if issubclass(OpenApiv13adgroupupdateAudienceRuleExclusions, dict):
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
        if not isinstance(other, OpenApiv13adgroupupdateAudienceRuleExclusions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
