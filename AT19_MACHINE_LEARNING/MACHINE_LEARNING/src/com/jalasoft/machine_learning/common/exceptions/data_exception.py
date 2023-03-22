# @data_exception.py Copyright (c) 2023 Jalasoft.
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

class DataException:
    """Wraps Exceptions"""
    def __init__(self, message: str, method_type: str):
        """Defines the constructor"""
        self.message: str = message
        self.method_type: str = method_type

    def assemble_message(self):
        """Assembly the message to show"""
        data_message = 'Machine learning data error: in ' + self.message + self.method_type
        return data_message
