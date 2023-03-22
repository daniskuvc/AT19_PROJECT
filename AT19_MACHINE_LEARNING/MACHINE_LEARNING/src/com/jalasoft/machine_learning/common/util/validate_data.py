#
# @validate_data.py Copyright (c) 2023 Jalasoft.
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

import cv2
from pathlib import Path
import requests
from common.exceptions.machine_learning_exception import MachineLearningException


class ValidateData:
    """Validates possible errors in other scripts"""
    def __init__(self, parameter: str, verify_list: list, class_of_refernce: str):
        """Defines the constructor"""
        self.parameter: str = parameter
        self.verify_list: list = verify_list
        self.class_of_reference: str = class_of_refernce

    def validate(self, exception_type):
        """Defines what is going to be validated"""
        dictionary = {'empty': self._validate_empty,
                      'dir': self._validate_dir,
                      'file': self._validate_file,
                      'img': self._validate_image,
                      'str': self._validate_str,
                      'int': self._validate_int,
                      'model': self._validate_object_model,
                      'model_feature': self._validate_feature_model,
                      'range_perc': self._validate_range_percentage
                      }
        for verify in self.verify_list:
            method_to_implement = dictionary[verify]
            method_to_implement(self.parameter, exception_type)

    def _validate_empty(self, data, exception_type):
        """Verifies the data is not empty"""
        if not data:
            raise MachineLearningException(self.class_of_reference, exception_type, ' can not be empty')

    def _validate_dir(self, data, exception_type):
        """Verifies the data is a valid directory"""
        data_path = Path(data)
        if not data_path.is_dir():
            raise MachineLearningException(self.class_of_reference, exception_type, ' must be directory')

    def _validate_file(self, data, exception_type):
        """Verifies the data is a valid file"""
        data_path = Path(data)
        if not data_path.is_file():
            raise MachineLearningException(self.class_of_reference, exception_type, ' must be a file')

    def _validate_image(self, data, exception_type):
        """Verifies the data is an image"""
        if cv2.imread(data) is None:
            raise MachineLearningException(self.class_of_reference, exception_type, ' must be an image')

    def _validate_str(self, data, exception_type):
        """Verifies the data is a string type"""
        if not isinstance(data, str):
            raise MachineLearningException(self.class_of_reference, exception_type, 'is not a str type')

    def _validate_int(self, data, exception_type):
        """Verifies the data is an int type"""
        if not data.isdigit():
            raise MachineLearningException(self.class_of_reference, exception_type, ' must be int')

    def _validate_object_model(self, data, exception_type):
        """Verifies the data is a valid object model to use"""
        if not (data == 'desnet' or data == 'resnet' or data == 'inception' or data == 'mobile'):
            raise MachineLearningException(self.class_of_reference, exception_type, ' is not a valid method')

    def _validate_feature_model(self, data, exception_type):
        """Verifies the data is a valid object model to use"""
        if not (data == 'face' or data == 'emotion' or data == 'gender' or data == 'race' or data == 'age'):
            raise MachineLearningException(self.class_of_reference, exception_type, ' is not a feature method')

    def _validate_range_percentage(self, data, exception_type):
        """Verifies range percentage"""
        data = int(data)
        if data < 1 or data > 100:
            raise MachineLearningException(self.class_of_reference, exception_type, ' is not in the range')
