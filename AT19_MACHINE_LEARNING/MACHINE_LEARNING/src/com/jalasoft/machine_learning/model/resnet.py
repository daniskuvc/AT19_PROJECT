#
# @resnet.py Copyright (c) 2023 Jalasoft.
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

import os
from imageai.Classification import ImageClassification
from common.exceptions.machine_learning_exception import MachineLearningException
from model.model import Model
from common.util.validate_data import ValidateData
from config import RESNET_MODEL_PATH

# NNM_path = str(os.getenv('NNM_PATH'))
# RESNET_MODEL = 'resnet50-19c8e357.pth'
# RESNET_MODEL_PATH = os.path.join(NNM_path, RESNET_MODEL)


class ResnetModel(Model):
    """ Represents Resnet model """
    def __init__(self, image_path: str):
        """Defines the constructor"""
        self.image_path: str = image_path
        
    def algorithm(self) -> tuple:
        """ Executes the Resnet algorithm """
        ValidateData(self.image_path, ['empty', 'file', 'img'], 'Resnet model, image_path').validate('data_exception')
        ValidateData(RESNET_MODEL_PATH, ['empty', 'file'], 'Resnet model, RESNET_MODEL_PATH').validate('data_exception')
        try:
            prediction = ImageClassification()
            prediction.setModelTypeAsResNet50()
            prediction.setModelPath(RESNET_MODEL_PATH)
            prediction.loadModel()
            predictions, probabilities = prediction.classifyImage(self.image_path, result_count = 10)  
            return predictions, probabilities
        except RuntimeError:
            raise MachineLearningException("The algorithm method in resnet model can't be executed ", "data_exception"
                                           , __name__)
