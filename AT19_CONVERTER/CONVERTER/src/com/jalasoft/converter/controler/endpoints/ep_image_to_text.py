#
# @ep_image_to_text.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# # All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from flask import request
from flask_restful import Resource
from src.com.jalasoft.converter.common.command_line import Command
from src.com.jalasoft.converter.common.exception.convert_exception import ConvertException
from src.com.jalasoft.converter.controler.mange_request import ManageData
from src.com.jalasoft.converter.model.image.image_to_text import ImageToTextConvert


class ImageToText(Resource):
    """Defines image to black and white class"""
    def post(self):
        """Convert image to black and white image"""
        try:
            files = ManageData().generate_path('imaPdftex-')
            if files:
                file_in, file_out, url = files[0], files[1].split('.')[0], files[2]
                output_extension = files[1].split('.')[1]
                lang = request.form["lang"]
                Command(ImageToTextConvert(file_in, file_out, lang, output_extension).convert()).run_cmd()
                response = {'download_URL': url}
                return response, 200
            else:
                response = {'error message': 'File is corrupted'}
                return response, 400
        except ConvertException as error:
            response = {'error_message': error.get_message()}
            return response, 400
