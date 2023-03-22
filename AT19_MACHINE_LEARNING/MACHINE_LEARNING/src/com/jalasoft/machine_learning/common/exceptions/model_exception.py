#
# @model_exception.py Copyright (c) 2023 Jalasoft.
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


class ModelException(Exception):
    """Wraps Exceptions"""
    def __init__(self, message):
        """Defines constructor"""
        super().__init__()
        self.message = message

    def get_message(self):
        """Returns message"""
        return self.message
