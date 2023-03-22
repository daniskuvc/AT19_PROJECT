#
# @person_requests.py Copyright (c) 2023 Jalasoft.
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
from common.util.validate_data import ValidateData
from config import UPLOAD_FOLDER
from flask import request

# upload_path = (os.getenv('UPLOADS_PATH'))


class DataRequest:
    """Defines attributes of ogbjects."""
    def __init__(self, unknown_image_path: str,
                 known_image_path: str,
                 know_name: str,
                 unknown_name: str,
                 known_name: str):
        """contructs the attributes of objects."""
        self.unknown_upload_path: str = unknown_image_path
        self.known_upload_path: str = known_image_path
        self.know_name: str = know_name
        self.unknown_name: str = unknown_name
        self.known_name: str = known_name


class RequestPersonData:
    """process the information of request. """
    def __init__(self, request: object):
        """contructs the attributes of objects."""
        self.request: object = request   

    def get_request_person(self) -> object:
        """Creates an object with the request information."""

        requested_data = {
            'method': request.method,
            'url': request.url,
            'headers': dict(request.headers),
            'form_data': dict(request.form),
            'args_data': dict(request.args),
            # 'json_payload': request.get_json(),
            'files': dict(request.files)
        }
        print("\n\n++++++++++++++++++++\n",requested_data)




        unknown_image = self.request.files['unknown_image']
        known_image = self.request.files['known_image']
        known_name = self.request.form['known_name']
        ValidateData(known_image, ['empty'], 'known_image').validate('data_exception')
        ValidateData(unknown_image, ['empty'], 'unknown_image').validate('data_exception')
        known_file = known_image.filename
        unknown_file = unknown_image.filename
        unknown_path = os.path.join(UPLOAD_FOLDER, unknown_file)
        known_path = os.path.join(UPLOAD_FOLDER, known_file)
        unknown_image.save(unknown_path)
        known_image.save(known_path)
        data = DataRequest(unknown_path, known_path, known_name, unknown_file, known_file)
        return data
    