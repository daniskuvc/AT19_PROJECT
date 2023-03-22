#
# @response_validator.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
#
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
import pathlib

from Desktop_Interface.src.com.jalasoft.desktop.common.exception.request_exception import RequestException
import os


class ValidateResponse:
    """Validate request responses"""
    def validate_machine_learning_response(self, response):
        """Validates that the request response is not empty"""
        if response == []:
            raise RequestException("Object not find")

    def validate_url_machine_learning(self, result_url):
        """Validates the machine learning URL response"""
        if not result_url:
            raise RequestException("URL response is empty")
        if result_url is None:
            raise RequestException("Invalid URL response")
        if not type(result_url) == str:
            raise RequestException("invalid response type")
        pass

    def validate_status_code_response(self, code):
        """Validates the request response status code"""
        if not code == 200:
            raise RequestException("Failed request")

    def validate_zip_converter_response(self, zip_file):
        """Validates the converter zip response"""
        if not zip_file:
            raise RequestException("The converter response is empty")
        if zip_file is None:
            raise RequestException("Invalid converter response")
        if not isinstance(zip_file, pathlib.WindowsPath):
            raise RequestException("invalid response type")
        _, file_extension = os.path.splitext(zip_file)
        if not file_extension == '.zip':
            raise RequestException("Invalid response extension")
