#
# @test_audio_increase_volume.py Copyright (c) 2023 Jalasoft.
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
from src.com.jalasoft.converter.common.exception.input_exception import InvalidInputException
from src.com.jalasoft.converter.model.audio.audio_increase_volume import IncreaseVolume


class TestAudioIncrease(unittest.TestCase):
    """Defines unit tests for image_flip.py module"""

    # def test_audio_increase_volume_valid_data(self):
    #     """Test the happy path"""
    #     audio_increase = IncreaseVolume(r'..\..\..\resources\navidad.wav', r'..\..\..\resources\navidad.mp3', 2)
    #     expected = r'ffmpeg -i ..\..\..\resources\navidad.wav -af "volume=2" ..\..\..\resources\navidad.mp3'
    #     self.assertEqual(expected, audio_increase.convert())

    def test_audio_increase_none_input(self):
        """Test when input is None"""
        audio_increase = IncreaseVolume(None, r'..\..\..\resources\navidad.mp3', 2)
        with self.assertRaises(InvalidInputException):
            audio_increase.convert()

    def test_audio_increase_none_output(self):
        """Test when output is None"""
        audio_increase = IncreaseVolume(r'..\..\..\resources\navidad.wav', None, 2)
        with self.assertRaises(InvalidInputException):
            audio_increase.convert()

    def test_audio_increase_null_input(self):
        """Test when input is null"""
        audio_increase = IncreaseVolume('', r'..\..\..\resources\navidad.mp3', 2)
        with self.assertRaises(InvalidInputException):
            audio_increase.convert()

    def test_audio_increase_null_output(self):
        """Test when output is null"""
        audio_increase = IncreaseVolume(r'..\..\..\resources\navidad.wav', '', 2)
        with self.assertRaises(InvalidInputException):
            audio_increase.convert()

    def test_audio_increase_no_str_output(self):
        """Test when output is not str"""
        audio_increase = IncreaseVolume(r'..\..\..\resources\navidad.wav', False, 2)
        with self.assertRaises(InvalidInputException):
            audio_increase.convert()

    def test_audio_increase_no_str_input(self):
        """Test when input is not a str"""
        audio_increase = IncreaseVolume(True, r'..\..\..\resources\navidad.mp3', 2)
        with self.assertRaises(InvalidInputException):
            audio_increase.convert()

    def test_audio_increase_no_file(self):
        """Test when input has not file"""
        audio_increase = IncreaseVolume(r'..\..\..\resources\ ', r'..\..\..\resources\navidad.mp3', 2)
        with self.assertRaises(InvalidInputException):
            audio_increase.convert()

    def test_audio_increase_invalid_extension_input(self):
        """Test when input is an invalid extension"""
        audio_increase = IncreaseVolume(r'..\..\..\resources\Whats.mp4', r'..\..\..\resources\navidad.mp3', 2)
        with self.assertRaises(InvalidInputException):
            audio_increase.convert()

    def test_audio_increase_invalid_extension_output(self):
        """Test when output is an invalid extension"""
        audio_increase = IncreaseVolume(r'..\..\..\resources\navidad.wav', r'..\..\..\resources\notification.mp4', 2)
        with self.assertRaises(InvalidInputException):
            audio_increase.convert()

    def test_audio_increase_invalid_output_path(self):
        """Test whe the output path is not valid"""
        audio_increase = IncreaseVolume(r'..\..\..\resources\navidad.wav', r'..\..\..\resourcess\navidad.mp3', 2)
        with self.assertRaises(InvalidInputException):
            audio_increase.convert()

    def test_audio_increase_invalid_input_path(self):
        """Test when input path does not exist"""
        audio_increase = IncreaseVolume(r'..\..\..\resourcess\navidad.wav', r'..\..\..\resources\navidad.mp3', 2)
        with self.assertRaises(InvalidInputException):
            audio_increase.convert()

    def test_audio_increase_none_mult(self):
        """Test when multiplier is none"""
        audio_increase = IncreaseVolume(r'..\..\..\resources\navidad.wav', r'..\..\..\resources\navidad.mp3', None)
        with self.assertRaises(InvalidInputException):
            audio_increase.convert()

    def test_audio_increase_no_int_extension_mult(self):
        """Test when multiplier is none"""
        audio_increase = IncreaseVolume(r'..\..\..\resources\navidad.wav', r'..\..\..\resources\navidad.mp3', False)
        with self.assertRaises(InvalidInputException):
            audio_increase.convert()
