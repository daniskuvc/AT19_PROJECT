#
# @test_checksum.py Copyright (c) 2023 Jalasoft.
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
from Desktop_Interface.src.com.jalasoft.desktop.common.exception.file_exception import FileException
from Desktop_Interface.src.com.jalasoft.desktop.controller.checksum import Checksum


class TestChecksum(unittest.TestCase):
    """Defines unit tests for converter.py module"""
    def test_checksum_invalid_request(self):
        """Test when path is invalid"""
        checksum = Checksum()
        path = r'C:Users/User/Downloads/WhatsAppVideo223-01-20.mp4'
        with self.assertRaises(FileException):
            checksum.checksum_generator_md5(path)

    def test_converter_valid_request_code(self):
        """Test the happy path"""
        path = r'C:/Users/User/Documents/Python/AT19/Desktop/AT19_DESKTOP/Desktop_Interface/test/com/resources/vd.mp4'
        response = Checksum().checksum_generator_md5(path)
        self.assertIsNotNone(response)