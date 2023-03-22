#
# @object.py Copyright (c) 2023 Jalasoft.
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
from common.exceptions.machine_learning_exception import MachineLearningException
from common.util.validate_data import ValidateData


class Object:
    """Defines the object"""

    def __init__(self, percentage, method, word, file_name, file_path):
        """Constructs the attributes of objects."""
        self.percentage = percentage
        self.method = method
        self.word = word
        self.file_name = file_name
        self.file_path = file_path

    def toDBCollection(self):
        """Gives format for store in database"""
        ValidateData(self.percentage, ['empty', 'int', 'range_perc'], 'percentage').validate('data_exception')
        ValidateData(self.method, ['empty', 'model'], 'method' + self.method).validate('data_exception')
        ValidateData(self.word, ['empty', 'str'], 'word to find').validate('data_exception')
        ValidateData(self.file_name, ['empty', 'str'], 'file_name').validate('data_exception')
        ValidateData(self.file_path, ['empty', 'file'], self.method + 'model, image_path').validate \
            ('data_exception')
        try:
            return {
                'percentage': self.percentage,
                'method': self.method,
                'word': self.word,
                'file_name': self.file_name,
                'file_path': self.file_path
            }
        except Exception:
            raise MachineLearningException('Data collection failed', 'data_exception', self.method)
