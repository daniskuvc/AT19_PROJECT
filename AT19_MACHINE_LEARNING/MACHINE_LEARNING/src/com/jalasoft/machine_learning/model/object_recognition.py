#
# @object_recognition.py Copyright (c) 2023 Jalasoft.
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

from model.recognizer import Recognizer
from model.inception import InceptionModel
from model.mobilenet import MobilenetModel
from model.densenet import DensenetModel
from model.resnet import ResnetModel
from common.util.validate_data import ValidateData

method_dictionary = {"resnet": ResnetModel,
                     "inception": InceptionModel,
                     "desnet": DensenetModel,
                     "mobile": MobilenetModel}


class Objects(Recognizer):
    """Creates objects according to method params."""
    def __init__(self, data: object):
        """Constructs the attributes of objects."""
        self.image_path: str = data.file_path
        self.word: str = data.word
        self.percentage: int = data.percentage
        self.file_name: str = data.file_name
        self.method: str = data.method
        
    def recognition(self) -> dict:
        """Executes the recognition algorithm according to method."""
        ValidateData(self.method, ['empty', 'model'], 'method' + self.method).validate('data_exception')
        ValidateData(self.image_path, ['empty', 'file', 'img'], self.method + 'model, image_path').validate\
            ('data_exception')
        model_class = method_dictionary[self.method]
        predictions, probabilities = model_class(self.image_path).algorithm()
        result = dict(zip(predictions, probabilities))   
        return result

    def find_word(self, dictionary: dict) -> int:
        """Finds the percentage of a word key on the dictionary"""
        ValidateData(self.word, ['empty', 'str'], 'word to find').validate('data_exception')
        result = dictionary.get(self.word)
        if result is None:
            result = 0
        return int(result)
