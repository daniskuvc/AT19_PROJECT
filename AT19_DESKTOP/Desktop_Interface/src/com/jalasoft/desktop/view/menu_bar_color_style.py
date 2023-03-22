#
# @menu_bar_color_style.py Copyright (c) 2023 Jalasoft.
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

from Desktop_Interface.src.com.jalasoft.desktop.config import CSS_COLOR_PATH, COLOR_PATH
import json


class ColorStyle:
    """Rewrites the color.json with the color style"""

    def __init__(self, app):
        """Defines the constructor"""
        self.app = app

    def color_style(self):
        """Selects the color style"""
        with open(CSS_COLOR_PATH, 'r') as css_file:
            self.app.setStyleSheet(css_file.read())
        with open(COLOR_PATH, "w") as f:
            json.dump(CSS_COLOR_PATH, f)