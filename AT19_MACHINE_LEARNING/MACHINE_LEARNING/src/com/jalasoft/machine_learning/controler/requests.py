#
# @requests.py Copyright (c) 2023 Jalasoft.
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
from flask import request
from common.exceptions.machine_learning_exception import \
    MachineLearningException
from model.object import Object
from factory_method.mongo_db import MongoDB
from common.util.validate_data import ValidateData
from config import UPLOAD_FOLDER

# upload_path = str(os.getenv('UPLOADS_PATH'))


class Data:
    """Defines attributes of objects."""
    def __init__(self, file_path: str, method: str, file_name, word: str = "word", percentage: int = 30):
        """constructs the attributes of objects."""
        self.file_path: str = file_path
        self.method: str = method
        self.file_name: str = file_name
        self.word: str = word
        self.percentage: int = int(percentage)


class RequestData:
    """process the information of request. """
    def __init__(self, request: object):
        """constructs the attributes of objects."""
        self.request: object = request

    def get_request_feature(self) -> object:
        """Creates an object with the request information."""

        requested_data = {
            'method': request.method,
            'url': request.url,
            'headers': dict(request.headers),
            'form_data': dict(request.form),
            # 'json_payload': request.get_json(),
            'files': dict(request.files)
        }
        print("\n\n++++++++++++++++++++\n",requested_data)

        file = self.request.files["image"]
        method = self.request.form["method"]
        ValidateData(file, ['empty'], 'image').validate('data_exception')
        ValidateData(method, ['empty', 'model_feature'], 'method ' + method).validate('data_exception')
        file_name = file.filename
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        file.save(file_path)
        data = Data(file_path, method, file_name)
        return data

    def get_request_object(self) -> object:
        """Creates objects with the request information."""

        requested_data = {
            'method': request.method,
            'url': request.url,
            'headers': dict(request.headers),
            'form_data': dict(request.form),
            # 'json_payload': request.get_json(),
            'files': dict(request.files)
        }
        print("\n\n++++++++++++++++++++\n",requested_data)

        file = self.request.files["image"]
        percentage = self.request.form["percentage"]
        method = self.request.form["method"]
        word = self.request.form["word"]
        ValidateData(file, ['empty'], 'image').validate('data_exception')
        file_name = file.filename
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        file.save(file_path)
        ValidateData(percentage, ['empty', 'int', 'range_perc'], 'percentage').validate('data_exception')
        data = Data(file_path, method, file_name, word, percentage)
        mongo = MongoDB()
        animal = Object(percentage, method, word, file_name, file_path)
        repository = mongo.create_database()
        repository.create(animal, 'objects')
        return data
