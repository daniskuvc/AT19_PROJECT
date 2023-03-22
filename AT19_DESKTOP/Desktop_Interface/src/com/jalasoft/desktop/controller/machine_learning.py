#
# @machine_learning.py Copyright (c) 2023 Jalasoft.
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
from pathlib import Path

from Desktop_Interface.src.com.jalasoft.desktop.common.response_validator import ValidateResponse
from Desktop_Interface.src.com.jalasoft.desktop.controller.unzip import UnZipFiles
from Desktop_Interface.src.com.jalasoft.desktop.config import PATH
from Desktop_Interface.src.com.jalasoft.desktop.config import DATA_PATH
from Desktop_Interface.src.com.jalasoft.desktop.common.file_validator import FileValidator
from Desktop_Interface.src.com.jalasoft.desktop.common.exception.request_exception import RequestException
import json
import os

UPLOAD_FOLDER_MACHINE = os.path.join(PATH, 'uploads_machine')
os.makedirs(UPLOAD_FOLDER_MACHINE,  exist_ok = True)


class MachineLearning:
    """Defines requests to machine learning"""
    def send_zip(self, percentagevalue, textcombomodelvalue, textwordvalue, zip_to_send_machine):
        """Sent zip to machine learning"""
        FileValidator(DATA_PATH).validate_file()
        ValidateResponse().validate_zip_converter_response(zip_to_send_machine)
        try:
            with open(DATA_PATH, "r") as f:
                data = json.load(f)
                url_ml = data["machine learning"]
            json_ml = {"percentage": percentagevalue, "method": textcombomodelvalue, "word": textwordvalue}
            file_ml = open(zip_to_send_machine, "rb")      
            r_ml = requests.post(url_ml, json_ml, files = {"image": file_ml})
            response = r_ml.json()
            code = r_ml.status_code
            return response, code
        except Exception:
            raise RequestException("Error to send the request")

    def get_zip(self, result_link):
        """get zip from machine learning"""
        ValidateResponse().validate_url_machine_learning(result_link)
        try:
            r_converter2 = requests.get(result_link)
            name_comig_zip = result_link.split('=')[1]
            filename = Path(UPLOAD_FOLDER_MACHINE, name_comig_zip)
            filename.write_bytes(r_converter2.content)
            save_uncompress_zip = UnZipFiles(filename, PATH, name_comig_zip).uncompress()
            code = r_converter2.status_code
            return save_uncompress_zip, code
        except Exception:
            raise RequestException("Error uncompress the zip")
