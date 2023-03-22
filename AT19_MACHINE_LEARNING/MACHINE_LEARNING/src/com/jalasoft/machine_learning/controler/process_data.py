#
# @process_data.py.py Copyright (c) 2023 Jalasoft.
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
from model.object_recognition import Objects
from common.zip_file import ZipFiles
from config import UPLOAD_FOLDER
from config import RESPONSE_FOLDER
# from config import HOST_ML
# from config import PORT_ML

# host_ml = str(os.getenv('HOST_ML'))
# port_ml = str(os.getenv('PORT_ML'))
# upload_folder = str(os.getenv('UPLOADS_PATH'))
# responses_path = str(os.getenv('RESPONSES_PATH'))


class ProcessImageFile:
    """process the folder of images to found a object into images."""
    def __init__(self, data: object, unzip_folder_path: str):
        """Defines the constructor"""
        self.data: object = data
        self.unzip_folder_path: str = unzip_folder_path
        self.answer_list: list = []

    def process(self):
        """process the folder and get the percentage for every image."""
        images_list = os.listdir(self.unzip_folder_path)
        result_file_name = str('result_' + self.data.file_name.split('.')[0])
        zip_folder = os.path.join(UPLOAD_FOLDER, result_file_name)
        response_image_path = os.path.join(zip_folder, result_file_name)
        os.makedirs(response_image_path, exist_ok=True)
        self.predict_images(images_list, response_image_path)
        answer_list, zip_name = self.ziper(result_file_name, zip_folder)
        return answer_list, zip_name

    def predict_images(self, images_list, response_image_path):
        """Predict a list of images"""
        for image in images_list:
            new_path = os.path.join(self.unzip_folder_path, image)
            self.data.file_path = new_path
            result = Objects(self.data)
            prediction = result.recognition()
            final_persentage = result.find_word(prediction)
            if int(final_persentage) >= int(self.data.percentage):
                source = os.path.join(self.unzip_folder_path, image)
                destine = os.path.join(response_image_path, image)
                os.replace(source, destine)
                data_result = self.process_result(final_persentage, image)
                self.answer_list.append(data_result)

    def ziper(self, result_file_name, zip_folder):
        """zips the images in a folder"""
        zip_name = ZipFiles(result_file_name.split('.')[0], zip_folder, RESPONSE_FOLDER).compress()
        return self.answer_list, zip_name

    def process_result(self, final_percentage: int, image: str) -> dict:
        """asemble the result data"""
        data = {'file_name': image,
                'second': str(int(image.split('.')[0])),
                'percentage': str(final_percentage)}
        return data
