#
# @checksum.py Copyright (c) 2023 Jalasoft.
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

import hashlib

from Desktop_Interface.src.com.jalasoft.desktop.common.exception.request_exception import RequestException
from Desktop_Interface.src.com.jalasoft.desktop.common.file_validator import FileValidator


class Checksum:
    """Defines the checksum generator"""
    def checksum_generator_md5(self, in_file):
        """Generates a checksum"""
        FileValidator(in_file).validate_file()
        try:
            with open(in_file, 'rb') as opened_file:
                content = opened_file.read()
                md5 = hashlib.md5()
                md5.update(content)
                check = md5.hexdigest()
            return check
        except Exception:
            raise RequestException("Error in the checksum")