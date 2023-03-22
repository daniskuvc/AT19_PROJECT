#
# @face_recognizer.py Copyright (c) 2023 Jalasoft.
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
import os
from common.exceptions.machine_learning_exception import MachineLearningException
from common.util.validate_data import ValidateData
from model.recognizer import Recognizer
from config import CASC_PATH
from config import RESPONSE_FOLDER

# responses = str(os.getenv('RESPONSES_PATH'))
# nnm_path = str(os.getenv('NNM_PATH'))
# cascPath = os.path.join(nnm_path, 'haarcascade_frontalface_default.xml')


class FaceRecognizer(Recognizer):
    """Class representing the Face Recognizer"""
    def __init__(self, data: object):
        """Defines the constructor"""
        self.data: object = data

    def recognition(self) -> dict:
        """Detects faces in the image"""
        ValidateData(self.data.file_path, ['empty', 'file', 'img'], 'feature file_path').validate('data_exception')
        ValidateData(self.data.file_name, ['empty', 'str'], 'feature file_name').validate('data_exception')
        try:
            faceCascade = cv2.CascadeClassifier(CASC_PATH)
            image = cv2.imread(self.data.file_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor = 1.1,
                minNeighbors = 5,
                minSize = (30, 30),
            )
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            result_file_name = 'result_' + self.data.file_name
            image_result_path = os.path.join(RESPONSE_FOLDER, result_file_name)
            cv2.imwrite(image_result_path, image)
            data = [{'totalFaces': len(faces)}]
            return data, result_file_name
        except Exception:
            raise MachineLearningException("The algorithm method in FaceRecognizer model can't be executed ",
                                           "data_exception", __name__)
