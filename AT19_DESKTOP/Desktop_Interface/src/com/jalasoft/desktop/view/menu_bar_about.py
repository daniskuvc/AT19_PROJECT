#
# @menu_bar_about.py Copyright (c) 2023 Jalasoft.
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


class About:
    """Creates the About popup"""
    def about_option(self):
        """Shows the version of the app and the credits"""
        about_popup = QMessageBox()
        about_popup.setWindowTitle("About")
        about_popup.setText("""CONVERT AND RECOGNITION STUDIO V1\n
            This app was made by AT-19 Team:\n
            Celeste Palet                       Carolina Vacaflor\n
            Daniel Villarroel                   David Garnica\n
            Denisse Cordova                 Fabian Cabrejo\n
            Leonardo Pacheco             Maria Mamani\n
            Martin Alvarez                     Rocio Morales\n
            Roger Renjifo                       Selmi Murana\n
            Telma Rios""")
        about_popup.setStandardButtons(QMessageBox.Ok)
        about_popup.setIcon(QMessageBox.Information)
        about_popup.setWindowIcon(QIcon(IMG_ICON_PATH))
        about_popup.exec_()
