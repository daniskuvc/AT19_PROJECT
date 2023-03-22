#
# @person_recognition.py Copyright (c) 2022 Jalasoft.
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
from model.recognizer import Recognizer
from common.util.validate_data import ValidateData
from config import RESPONSE_FOLDER

# responce_path = os.getenv('RESPONSES_PATH')


class Person(Recognizer):
    """Recognizes a know person from a image"""
    def __init__(self, data):
        """Defines the constructor"""
        super().__init__(data)
        ValidateData(data.known_upload_path, ['empty', 'file', 'img'], 'Known_image').validate('data_exception')
        ValidateData(data.unknown_upload_path, ['empty', 'file', 'img'], 'unKnown_image').validate('data_exception')
        self.known_image = face_recognition.load_image_file(data.known_upload_path)
        self.input_image = face_recognition.load_image_file(data.unknown_upload_path)
        self.known_name = data.know_name

    def recognition(self):
        """Detects a know face in an image"""
        ValidateData(self.known_name, ['empty', 'str'], 'known_name').validate('data_exception')
        ValidateData(self.data.unknown_name, ['empty', 'str'], 'name unknown_image').validate('data_exception')
        ValidateData(self.data.known_name, ['empty', 'str'], 'name known_image').validate('data_exception')
        face_locations = face_recognition.face_locations(self.known_image)
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(self.known_image, (left, top), (right, bottom), (0, 255, 0), 2)

        face_landmarks_list = face_recognition.face_landmarks(self.known_image)
        facial_features = ['chin', 'left_eyebrow', 'right_eyebrow', 'nose_bridge', 'left_eye',
                           'right_eye', 'top_lip', 'bottom_lip']
        for face_landmarks in face_landmarks_list:
            for facial_feature in facial_features:
                for point in face_landmarks[facial_feature]:
                    self.known_image = cv2.circle(self.known_image, point, 2, (255, 60, 170), 2)

        image_encoding = face_recognition.face_encodings(self.known_image)[0]
        unknown_encoding = face_recognition.face_encodings(self.input_image)[0]
        results = face_recognition.compare_faces([image_encoding], unknown_encoding)
        print(f'{self.known_name}: {results[0]}')
        cv2.putText(self.input_image, f'{self.known_name}: {results[0]}', (25, 75),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 1)
        result_file_name = "result_" + self.data.unknown_name
        image_result_path = os.path.join(RESPONSE_FOLDER, result_file_name)
        cv2.imwrite(image_result_path, cv2.cvtColor(self.input_image, cv2.COLOR_BGR2RGB))
        recognition_result = [{'person': self.data.know_name, 'result': str(results[0])}]
        return recognition_result, result_file_name
