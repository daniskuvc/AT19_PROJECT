#
# @test_machine_learning.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# # All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import unittest

from Desktop_Interface.src.com.jalasoft.desktop.common.exception.request_exception import RequestException
from Desktop_Interface.src.com.jalasoft.desktop.controller.machine_learning import MachineLearning


class TestMachineLearning(unittest.TestCase):
    """Defines unit tests for machine_learning.py module"""
    def test_machine_validate_code_get_zip(self):
        """Test the happy path"""
        url = 'http://127.0.0.1:5001/download?file_name=result_WhatsApp_Video_2023-01-20.zip'
        machine_response, code = MachineLearning().get_zip(url)
        self.assertEqual(200, code)

    def test_empty_data_send_zip(self):
        """Test when the zip is null"""
        machine_learning = MachineLearning()
        with self.assertRaises(RequestException):
            machine_learning.send_zip('43', 'desnet', 'cat', '')

    def test_none_data_send_zip(self):
        """Test when the zip is none"""
        machine_learning = MachineLearning()
        with self.assertRaises(RequestException):
            machine_learning.send_zip('52', 'inception', 'microphone', None)

    def test_number_send_zip(self):
        """Test when sends a number instead of a zip """
        machine_learning = MachineLearning()
        with self.assertRaises(RequestException):
            machine_learning.send_zip('59', 'resnet', 'pineapple', 5651)

    def test_invalid_data_send_zip(self):
        """Test when sends a song instead of a zip"""
        machine_learning = MachineLearning()
        with self.assertRaises(RequestException):
            machine_learning.send_zip('59', 'mobile', 'pineapple', 'C:/Users/User/Documents/Python/AT19/song.mp3')

    def test_no_str_get_zip(self):
        """Test When the URL is a number"""
        machine_learning = MachineLearning()
        with self.assertRaises(RequestException):
            machine_learning.get_zip(435)

    def test_empty_data_get_zip(self):
        """Test when the URL is null"""
        machine_learning = MachineLearning()
        with self.assertRaises(RequestException):
            machine_learning.get_zip('')

    def test_none_data_get_zip(self):
        """Test when the URL is none"""
        machine_learning = MachineLearning()
        with self.assertRaises(RequestException):
            machine_learning.get_zip(None)