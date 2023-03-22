# @machine_learning_exception.py Copyright (c) 2023 Jalasoft.
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

from common.exceptions.data_exception import DataException
from common.exceptions.model_exception import ModelException


class MachineLearningException(Exception):
    """Machine learning to content all exceptions"""
    def __init__(self, message: str, exception_type: str, method_type: str):
        """Defines the constructor"""
        super().__init__()
        self.message: str = message
        self.exception_type: str = exception_type
        self.method_type: str = method_type

    def get_message(self):
        """Returns message"""
        exceptions = {'data_exception': DataException,
                      'model_exception': ModelException}

        exception_to_implement = exceptions[self.exception_type]
        result_message = exception_to_implement(self.message, self.method_type).assemble_message()
        return result_message
