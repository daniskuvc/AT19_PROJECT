#
# @url_validation.py Copyright (c) 2023 Jalasoft.
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

from Desktop_Interface.src.com.jalasoft.desktop.common.exception.input_exception import InvalidInputException


class UrlValidator:
    """Validate URLs of converter and machine learning"""
    def __init__(self, url_converter, url_machine):
        """Defines the constructor"""
        self.url_converter = url_converter
        self.url_machine = url_machine

    def validate_url(self):
        """Validates that the URLs are not empty"""
        if self.url_converter == '':
            raise InvalidInputException("Invalid Converter URL")
        if self.url_machine == '':
            raise InvalidInputException("Invalid Machine Learning URL")
    