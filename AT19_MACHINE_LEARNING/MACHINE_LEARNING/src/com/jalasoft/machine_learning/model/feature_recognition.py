#
# @feature_recognition.py Copyright (c) 2023 Jalasoft.
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
import cv2
import face_recognition
from deepface import DeepFace
from retinaface import RetinaFace
from model.recognizer import Recognizer
from common.util.validate_data import ValidateData
from config import RESPONSE_FOLDER

# responce_path = os.getenv('RESPONSES_PATH')


class Feature(Recognizer):
    """Generates an object to feature recognition."""

    def __init__(self, data: object):
        """constructs the attributes of objects."""
        super().__init__(data)

    def recognition(self) -> list:
        """Detects features on faces in the image"""
        ValidateData(self.data.file_path, ['empty', 'file', 'img'], 'feature file_path').validate('data_exception')
        ValidateData(self.data.method, ['empty', 'model_feature'], 'method ' + self.data.method).validate\
            ('data_exception')
        img = cv2.imread(self.data.file_path)
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        found_faces = RetinaFace.extract_faces(img_path=image, align=True)

        recognition_result = []
        for face in found_faces:
            tmp_result = DeepFace.analyze(img_path=face, actions=[self.data.method], enforce_detection=False)[0]
            print("++++++++++++++++++++++", tmp_result)

            if self.data.method == "race" or self.data.method == "emotion" or self.data.method == "gender":
                recognition_result.append({self.data.method: {tmp_result["dominant_" + self.data.method]: tmp_result[self.data.method][tmp_result["dominant_" + self.data.method]]}})
            else:
                recognition_result.append({self.data.method: tmp_result[self.data.method]})

        face_locations = face_recognition.face_locations(image)
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        result_file_name: str = "result_" + self.data.file_name
        image_result_path = os.path.join(RESPONSE_FOLDER, result_file_name)
        cv2.imwrite(image_result_path, cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        return recognition_result, result_file_name
