#
# @ep_video_to_zip_image.py Copyright (c) 2023 Jalasoft.
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
from src.com.jalasoft.converter.common.zip_file import ZipFiles
from config import RESPONSE_FOLDER
from config import DOWNLOAD_DIR
from src.com.jalasoft.converter.controler.mange_request import ManageData
from src.com.jalasoft.converter.model.video.vconverter import VideoToImages


class VideoToZipImage(Resource):
    """Defines video to zip class"""

    def post(self):
        """Create zip file containing image from video"""
        try:
            files = ManageData().generate_path('vidToima-')
            if files:
                file_in, file_out, url = files[0], files[1], files[2]
                fps = str(request.form["fps"])
                Command(VideoToImages(file_in, file_out, fps).convert()).run_cmd()
                tmp_zip = ZipFiles(file_in.split('.')[0], file_in.split('.')[0] + os.sep, RESPONSE_FOLDER).compress()
                url = DOWNLOAD_DIR + os.path.basename(tmp_zip)
                return {'download_URL': url}
            else:
                response = {'error message': 'File is corrupted'}
                return response, 400
        except ConvertException as error:
            response = {'error_message': error.get_message()}
            return response, 400
