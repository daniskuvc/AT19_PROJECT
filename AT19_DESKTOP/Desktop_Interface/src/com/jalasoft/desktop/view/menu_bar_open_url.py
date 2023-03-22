#
# @menu_bar_open_url.py Copyright (c) 2023 Jalasoft.
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
from Desktop_Interface.src.com.jalasoft.desktop.config import IMG_ICON_PATH


class OpenUrl:
    """Creates the URL popup"""
    def open_url_option(self):
        """Displays an informational message"""
        popup = QMessageBox()
        popup.setWindowTitle("Open URL")
        popup.setText("Please paste an URL in the Video Path text field.")
        popup.setStandardButtons(QMessageBox.Ok)
        popup.setIcon(QMessageBox.Information)
        popup.setWindowIcon(QIcon(IMG_ICON_PATH))
        popup.exec_()