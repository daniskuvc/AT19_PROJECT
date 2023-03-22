#
# @zip_file.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft
#

import shutil
import os
from common.exceptions.machine_learning_exception import MachineLearningException
from common.util.validate_data import ValidateData


class ZipFiles:
    """Defines ZipFiles criteria"""
    def __init__(self, name_of_zip: str, folder_to_zip: str, destination: str):
        """Defines the constructor"""
        self.name_of_zip: str = name_of_zip
        self.folder_to_zip: str = folder_to_zip
        self.destination: str = destination
    
    def compress(self) -> str:
        """Defines compress method"""
        ValidateData(self.folder_to_zip, ['empty', 'dir'], 'zip_file.py, folder to zip').validate('data_exception')
        try:
            shutil.make_archive(self.name_of_zip, 'zip', self.folder_to_zip)
            name = self.name_of_zip + '.zip'
            shutil.move(name, os.path.join(self.destination, os.path.basename(name)))
            return name
        except Exception:
            raise MachineLearningException('It is not a valid type file to zip', 'data_exception', self.path_of_zip)
    