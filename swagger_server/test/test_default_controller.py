# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.lecture import Lecture  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_uni_get_day_lectures(self):
        """Test case for uni_get_day_lectures

        Get the Lectures of the Current(+offset) Day
        """
        response = self.client.open(
            '/patrickstecker/SmartJoeServer/1.0.0/uni/lectures/day/{offset}'.format(offset=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_uni_get_days_around_lectures(self):
        """Test case for uni_get_days_around_lectures

        Get Lecture-Days around today(+offset) in range of range
        """
        response = self.client.open(
            '/patrickstecker/SmartJoeServer/1.0.0/uni/lectures/daysAroundToday/{offset}/{range}'.format(offset=1.2, range=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_uni_get_week_lectures(self):
        """Test case for uni_get_week_lectures

        Get the Lectures of the Current Week(+offset)
        """
        response = self.client.open(
            '/patrickstecker/SmartJoeServer/1.0.0/uni/lectures/week/{offset}'.format(offset=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
