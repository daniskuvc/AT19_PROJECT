#
# @test_audio_converter.py Copyright (c) 2023 Jalasoft.
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
from CONVERTER.src.com.jalasoft.converter.common.exception.input_exception import InvalidInputException
from CONVERTER.src.com.jalasoft.converter.model.audio.audio_converter import AudioConvert


class TestAudioConvert(unittest.TestCase):
    """Defines unit tests for image_flip.py module"""

    # def test_audio_convert_valid_data(self):
    #     """Test the happy path"""
    #     audio_convert = AudioConvert(r'..\..\..\resources\navidad.wav', r'..\..\..\resources\navidad.mp3')
    #     expected = r'ffmpeg -i ..\..\..\resources\navidad.wav ..\..\..\resources\navidad.mp3'
    #     self.assertEqual(expected, audio_convert.convert())

    def test_audio_convert_none_input(self):
        """Test when input is None"""
        audio_convert = AudioConvert(None, r'..\..\..\resources\navidad.mp3')
        with self.assertRaises(InvalidInputException):
            audio_convert.convert()

    def test_audio_convert_none_output(self):
        """Test when output is None"""
        audio_convert = AudioConvert(r'..\..\..\resources\navidad.wav', None)
        with self.assertRaises(InvalidInputException):
            audio_convert.convert()

    def test_audio_convert_null_input(self):
        """Test when input is null"""
        audio_convert = AudioConvert('', r'..\..\..\resources\navidad.mp3')
        with self.assertRaises(InvalidInputException):
            audio_convert.convert()

    def test_audio_convert_null_output(self):
        """Test when output is null"""
        audio_convert = AudioConvert(r'..\..\..\resources\navidad.wav', '')
        with self.assertRaises(InvalidInputException):
            audio_convert.convert()

    def test_audio_convert_no_str_output(self):
        """Test when output is not str"""
        audio_convert = AudioConvert(r'..\..\..\resources\navidad.wav', False)
        with self.assertRaises(InvalidInputException):
            audio_convert.convert()

    def test_audio_convert_no_str_input(self):
        """Test when input is not a str"""
        audio_convert = AudioConvert(2, r'..\..\..\resources\navidad.mp3')
        with self.assertRaises(InvalidInputException):
            audio_convert.convert()

    def test_audio_convert_no_file(self):
        """Test when input has not file"""
        audio_convert = AudioConvert(r'..\..\..\resources\ ', r'..\..\..\resources\navidad.mp3')
        with self.assertRaises(InvalidInputException):
            audio_convert.convert()

    def test_audio_convert_invalid_extension_input(self):
        """Test when input is an invalid extension"""
        audio_convert = AudioConvert(r'..\..\..\resources\Image.jpg', r'..\..\..\resources\navidad.mp3')
        with self.assertRaises(InvalidInputException):
            audio_convert.convert()

    def test_audio_convert_invalid_extension_output(self):
        """Test when output is an invalid extension"""
        audio_convert = AudioConvert(r'..\..\..\resources\navidad.wav', r'..\..\..\resources\Image.jpg')
        with self.assertRaises(InvalidInputException):
            audio_convert.convert()

    def test_audio_convert_invalid_output_path(self):
        """Test whe the output path is not valid"""
        audio_convert = AudioConvert(r'..\..\..\resources\navidad.wav', r'../../../resourcess/navidad.mp3')
        with self.assertRaises(InvalidInputException):
            audio_convert.convert()

    # def test_audio_convert_invalid_input_path(self):
    #     """Test when input path does not exist"""
    #     audio_convert = AudioConvert(r'../../../resourcess/navidad.wav', r'..\..\..\resources\navidad.mp3')
    #     with self.assertRaises(InvalidInputException):
    #         audio_convert.convert()
