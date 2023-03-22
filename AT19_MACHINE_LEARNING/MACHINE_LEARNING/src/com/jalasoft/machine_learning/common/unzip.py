#
# @unzip.py Copyright (c) 2023 Jalasoft.
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

import zipfile
import os
from common.exceptions.machine_learning_exception import MachineLearningException
from common.util.validate_data import ValidateData


class UnZipFiles:
    """Defines UnZipFiles criteria"""
    def __init__(self, path_of_zip: str, destination: str, zip_name: str):
        """Defines the constructor"""
        self.path_of_zip: str = path_of_zip
        self.destination: str = destination    
        self.zip_name: str = zip_name
        
    def uncompress(self) -> str:
        """Defines Un-compress method"""
        ValidateData(self.path_of_zip, ['empty', 'file'], 'The zip file').validate('data_exception')
        try:
            with zipfile.ZipFile(self.path_of_zip, 'r') as zip_ref:
                zip_ref.extractall(self.destination)
            new_path = os.path.join(self.destination, self.zip_name.split('.')[0])
            return new_path
        except Exception:
            raise MachineLearningException('It is not a type .zip file ', 'data_exception', self.path_of_zip)
