#
# @result.py Copyright (c) 2023 Jalasoft.
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
from flask import jsonify
from config import DOWNLOAD_DIR

# host_ml: str = str(os.getenv('HOST_ML'))
# port_ml: str = str(os.getenv('PORT_ML'))


class ResultData:
    """Process results"""
    def __init__(self, list: list, file_name: str):
        """Defines class attributes."""
        self.result_list: list = list
        self.file_name: str = file_name

    def result(self) -> dict:
        """Assembles result """
        # url: str = 'http://' + host_ml + ':' + port_ml + '/download?file_name='
        final_result: dict = {'list': self.result_list, 'url': (DOWNLOAD_DIR + self.file_name)}
        return jsonify(final_result)
