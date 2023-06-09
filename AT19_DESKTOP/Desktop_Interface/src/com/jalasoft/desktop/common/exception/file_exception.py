#
# @file_exception.py Copyright (c) 2023 Jalasoft.
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

from Desktop_Interface.src.com.jalasoft.desktop.common.exception.pyqt_exception import PyqtException


class FileException(PyqtException):
    """Defines exception criteria"""
    def __init__(self, message):
        super().__init__(message)

    def get_message(self):
        """Send the message for the exception"""
        return self.message
