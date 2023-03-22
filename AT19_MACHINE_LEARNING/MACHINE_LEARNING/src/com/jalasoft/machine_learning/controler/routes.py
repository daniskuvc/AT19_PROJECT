#
# @routes.py Copyright (c) 2023 Jalasoft.
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
from flask import jsonify
from flask import make_response
from flask import request
from flask import send_from_directory
from flask_restful import Resource
from model.face_recognizer import FaceRecognizer
from model.person_recognition import Person
from model.feature_recognition import Feature
from controler.requests import RequestData
from controler.person_requests import RequestPersonData
from controler.process_data import ProcessImageFile
from controler.result import ResultData
from common.unzip import UnZipFiles
from common.exceptions.machine_learning_exception import MachineLearningException
from config import RESPONSE_FOLDER


class PersonRecognizer(Resource):
    """Get into it when /person_recognizer endpoint is requested"""
    def post(self) -> dict:
        """Returns true if two images are the same person."""
        try:
            data = RequestPersonData(request).get_request_person()
            recognition_result, result_file_name = Person(data).recognition()
            result: jsonify = ResultData(recognition_result, result_file_name).result()
            return result
        except MachineLearningException as error:
            return make_response(jsonify(Machine_learning_error = error.get_message()), 400)


class FeatureFaceRecognition(Resource):
    """Get into it when /feature_recognizer endpoint is requested"""
    def post(self):
        """Recognizes person face, emotion and gender on an image."""
        try:
            data: object = RequestData(request).get_request_feature()
            dictionary = {"face": FaceRecognizer, "emotion": Feature, "gender": Feature, "race": Feature,
                          "age": Feature}
            model_class = dictionary[data.method]
            recognizer = model_class(data)
            recognition_result, result_file_name = recognizer.recognition()
            result: jsonify = ResultData(recognition_result, result_file_name).result()
            return result
        except MachineLearningException as error:
            return make_response(jsonify(Machine_learning_error = error.get_message()), 400)


class ObjectRecognizer(Resource):
    """Get into it when /object_recognizer endpoint is requested"""
    def post(self) -> make_response:
        """Returns the probability and where the image is according to the post request petition."""
        try:
            data = RequestData(request).get_request_object()
            unzip_folder_path = UnZipFiles(data.file_path, RESPONSE_FOLDER, data.file_name).uncompress()
            recognition_result, result_file_name = ProcessImageFile(data, unzip_folder_path).process()
            result: jsonify = ResultData(recognition_result, result_file_name).result()
            return result
        except MachineLearningException as error:
            return make_response(jsonify(Machine_learning_error = error.get_message()), 400)


class Download(Resource):
    """Defines download file method --> url"""
    def get(self) -> __file__:
        """Downloads file"""
        file_name = request.args["file_name"]
        return send_from_directory(directory=RESPONSE_FOLDER, path=file_name, as_attachment=False)
