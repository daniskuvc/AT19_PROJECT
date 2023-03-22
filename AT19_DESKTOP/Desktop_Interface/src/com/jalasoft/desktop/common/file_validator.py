#
# @file_validator.py Copyright (c) 2023 Jalasoft.
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

from Desktop_Interface.src.com.jalasoft.desktop.common.exception.file_exception import FileException
import os


class FileValidator:
    """Validate files"""
    def __init__(self, file):
        """Defines the constructor"""
        self.file = file

    def validate_file(self):
        """Validates the existence of the file in the folder"""
        if not os.path.exists(self.file):
            raise FileException("File not found")
