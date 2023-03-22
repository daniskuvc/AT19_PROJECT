#
# @menu_bar_dark_style.py Copyright (c) 2023 Jalasoft.
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

from Desktop_Interface.src.com.jalasoft.desktop.config import CSS_DARK_PATH, COLOR_PATH
import json


class DarkStyle:
    """Rewrites the color.json with the dark style"""
    def __init__(self, app):
        """Defines the constructor"""
        self.app = app

    def dark_style(self):
        """Selects the dark style"""
        with open(CSS_DARK_PATH, 'r') as css_file:
            self.app.setStyleSheet(css_file.read())
        with open(COLOR_PATH, "w") as f:
            json.dump(CSS_DARK_PATH, f)