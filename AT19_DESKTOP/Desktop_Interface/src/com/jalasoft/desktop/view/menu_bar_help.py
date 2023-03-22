#
# @menu_bar_help.py Copyright (c) 2023 Jalasoft.
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


class Help:
    """Creates the help popup"""
    def help_option(self):
        """Shows how to use the app"""
        help_popup = QMessageBox()
        help_popup.setWindowTitle("Help")
        help_popup.setText("""GET TO KNOW ABOUT CONVERT AND RECOGNITION STUDIO\n
                1. Click on 'Browse' button and look for a video.
                2. In the field 'Word' write the object that you want to
                    find into the video.
                3. In the field 'Per.%' write the coincidence percentage
                    you want.
                4. In the dropdown 'Output Format' choose the image
                    format.
                5. In the dropdown 'Neural Model' choose the model
                    to use.
                6. Click on the 'Search' button.
                7. If you want to do a new search click on
                    'New Search'. This action will delete the last
                     results.""")
        help_popup.setStandardButtons(QMessageBox.Ok)
        help_popup.setIcon(QMessageBox.Information)
        help_popup.setWindowIcon(QIcon(IMG_ICON_PATH))
        help_popup.exec_()