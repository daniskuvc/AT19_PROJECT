#
# @converter.py Copyright (c) 2023 Jalasoft.
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

import requests
import os
from pathlib import Path
from Desktop_Interface.src.com.jalasoft.desktop.common.validate import ValidateInput
from Desktop_Interface.src.com.jalasoft.desktop.config import PATH, DATA_PATH
from Desktop_Interface.src.com.jalasoft.desktop.common.file_validator import FileValidator
from Desktop_Interface.src.com.jalasoft.desktop.common.exception.request_exception import RequestException
from Desktop_Interface.src.com.jalasoft.desktop.controller.checksum import Checksum
import json

UPLOAD_FOLDER_CONVERTER = os.path.join(PATH, 'uploads_converter')
os.makedirs(UPLOAD_FOLDER_CONVERTER,  exist_ok = True)


class Converter:
    """Defines requests to converter"""
    def get_token(self):
        """Generates token"""
        FileValidator(DATA_PATH).validate_file()
        try:
            json_token = {"username": "converter_user", "password": "1234"}
            with open(DATA_PATH, "r") as f:
                data = json.load(f)
            url_token = data["token"]
            token = requests.post(url_token, data = json_token).json()
            return token['token']
        except Exception:
            raise RequestException("Error to send login request")
    
    def get_zip(self, textcomboformatvalue, textboxvideopathvalue):
        """Sent video to converter"""
        FileValidator(DATA_PATH).validate_file()
        ValidateInput().validate_video_path(textboxvideopathvalue)
        try:
            token1 = self.get_token()
            header = {
                'Authorization': 'Bearer ' + token1
            }
            with open(DATA_PATH, "r") as f:
               data = json.load(f)
            url_converter = data["converter"]
            video_path_checksum = Checksum().checksum_generator_md5(textboxvideopathvalue)
            json_converter = {"output_file": textcomboformatvalue, "fps": 1, "checksum_param": video_path_checksum}
            file_converter = open(textboxvideopathvalue, "rb")
            converter_response_post = requests.post(url_converter, data = json_converter,
                                                    files = {"input_file": file_converter}, headers = header).json()
            url_to_download = converter_response_post['download_URL']
            url_file_name = url_to_download.split('=')[1]
            converter_response_get = requests.get(url_to_download)
            save_zip_converter = Path(UPLOAD_FOLDER_CONVERTER, url_file_name)
            save_zip_converter.write_bytes(converter_response_get.content)
            code_converter = converter_response_get.status_code
            return save_zip_converter, code_converter
        except Exception:
            raise RequestException("Error to send the request")

