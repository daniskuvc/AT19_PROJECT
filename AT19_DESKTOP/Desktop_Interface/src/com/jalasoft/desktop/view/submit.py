#
# @submit.py Copyright (c) 2023 Jalasoft.
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

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from Desktop_Interface.src.com.jalasoft.desktop.common.exception.pyqt_exception import PyqtException
from Desktop_Interface.src.com.jalasoft.desktop.common.url_validation import UrlValidator
from Desktop_Interface.src.com.jalasoft.desktop.config import DATA_PATH, IMG_ICON_PATH
import json


class SubmitButton:
    """Rewrites the data.json with the new URLs"""
    def submit(self, text1, text2):
        """Sets URLs"""
        try:
            UrlValidator(text1, text2).validate_url()
            data = {"converter": text1, "machine learning": text2}
            with open(DATA_PATH, "w") as f:
                json.dump(data, f)
            url_set_popup = QMessageBox()
            url_set_popup.setWindowTitle("URL set")
            url_set_popup.setText("""New URL was set""")
            url_set_popup.setIcon(QMessageBox.Information)
            url_set_popup.setWindowIcon(QIcon(IMG_ICON_PATH))
            url_set_popup.exec_()
        except PyqtException as error:
            error_popup = QMessageBox()
            error_popup.setWindowTitle("Error")
            error_popup.setText(error.get_message())
            error_popup.setWindowIcon(QIcon(IMG_ICON_PATH))
            error_popup.exec_()