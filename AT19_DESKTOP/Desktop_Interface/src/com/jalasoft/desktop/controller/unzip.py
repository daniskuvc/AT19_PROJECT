#
# @unzip.py Copyright (c) 2021 Jalasoft.
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

import shutil
import os

from Desktop_Interface.src.com.jalasoft.desktop.common.exception.request_exception import RequestException


class UnZipFiles:
    """Defines UnZipFiles criteria"""
    def __init__(self, path_of_zip,destination,zip_name):
        self.path_of_zip = path_of_zip
        self.destination = destination    
        self.zip_name=zip_name

    def uncompress(self):
        """Defines Un-compress method"""
        try:
            shutil.unpack_archive(self.path_of_zip, self.destination)
            new_path = os.path.join(self.destination, self.zip_name.split('.')[0])
            return new_path
        except Exception:
            raise RequestException("Unzip error")
