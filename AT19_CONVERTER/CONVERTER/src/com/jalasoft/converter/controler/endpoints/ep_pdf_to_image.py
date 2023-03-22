#
# @ep_pdf_to_image.py Copyright (c) 2023 Jalasoft.
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
from flask_restful import Resource
from src.com.jalasoft.converter.common.command_line import Command
from src.com.jalasoft.converter.common.exception.convert_exception import ConvertException
from src.com.jalasoft.converter.controler.mange_request import ManageData
from src.com.jalasoft.converter.model.image.pdf_to_image import PdfImage
from src.com.jalasoft.converter.common.zip_file import ZipFiles
from config import RESPONSE_FOLDER
from config import DOWNLOAD_DIR

class PdfToImage(Resource):
    """Defines image to black and white class"""
    def post(self):
        """Convert image to black and white image"""
        try:
            files = ManageData().generate_path('pdfToima-')
            if files:
                file_in, file_out, url = files[0], files[1], files[2]
                quality = request.form["quality"]
                Command(PdfImage(file_in, file_out, quality).convert()).run_cmd()
                tmp_zip = ZipFiles(file_in.split('.')[0], file_in.split('.')[0] + os.sep, RESPONSE_FOLDER).compress()
                url = DOWNLOAD_DIR + os.path.basename(tmp_zip)                
                return {'download_URL': url}
            else:
                response = {'error message': 'File is corrupted'}
                return response, 400
        except ConvertException as error:
            response = {'error_message': error.get_message()}
            return response, 400
