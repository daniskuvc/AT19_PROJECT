#
# @main.py Copyright (c) 2023 Jalasoft.
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

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from view.main_window import Window
from config import COLOR_PATH
from config import IMG_ICON_PATH
from common.file_validator import FileValidator
from common.exception.pyqt_exception import PyqtException
import sys
import json


try:
    app = QApplication(sys.argv)
    FileValidator(COLOR_PATH).validate_file()
    with open(COLOR_PATH, "r") as f:
        data = json.load(f)
    with open(data, 'r') as css_file:
        app.setStyleSheet(css_file.read())
    window = Window(app)
    sys.exit(app.exec_())
except PyqtException as error:
    error_popup = QMessageBox()
    error_popup.setWindowTitle("Error")
    error_popup.setText(error.get_message())
    error_popup.setWindowIcon(QIcon(IMG_ICON_PATH))
    error_popup.exec_()
