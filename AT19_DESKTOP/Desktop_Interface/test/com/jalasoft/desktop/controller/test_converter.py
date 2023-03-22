#
# @test_converter.py Copyright (c) 2023 Jalasoft.
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
from requests import RequestException
from Desktop_Interface.src.com.jalasoft.desktop.common.exception.input_exception import InvalidInputException
from Desktop_Interface.src.com.jalasoft.desktop.common.exception.request_exception import RequestException
from Desktop_Interface.src.com.jalasoft.desktop.controller.converter import Converter


class TestConverter(unittest.TestCase):
    """Defines unit tests for converter.py module"""
    def test_converter_invalid_request(self):
        """Test when format is invalid"""
        converter = Converter()
        with self.assertRaises(RequestException):
            converter.get_zip('invalid', r'C:/Users/User/Downloads/WhatsApp Video 2023-01-20.mp4')

    def test_converter_valid_request_code(self):
        """Test the happy path"""
        path = r'C:/Users/User/Documents/Python/AT19/Desktop/AT19_DESKTOP/Desktop_Interface/test/com/resources/vd.mp4'
        print(path)
        converter, code = Converter().get_zip('jpg', path)
        self.assertEqual(200, code)

    def test_converter_empty_video_path(self):
        """Test when the video path is null"""
        converter = Converter()
        with self.assertRaises(InvalidInputException):
            converter.get_zip('png', '')

    def test_converter_folder_video_path(self):
        """Test when the video path is a folder"""
        converter = Converter()
        with self.assertRaises(InvalidInputException):
            converter.get_zip('png', 'C:/Users/User/Documents/Python/AT19/Desktop')

    def test_converter_invalid_extension_video_path(self):
        """Test when the video path does not have a video extension"""
        converter = Converter()
        with self.assertRaises(InvalidInputException):
            converter.get_zip('png', 'C:/Users/User/Documents/song.mp3')
