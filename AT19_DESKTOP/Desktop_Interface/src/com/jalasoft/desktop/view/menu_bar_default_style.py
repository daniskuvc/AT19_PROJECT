#
# @menu_bar_default_style.py Copyright (c) 2023 Jalasoft.
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

from Desktop_Interface.src.com.jalasoft.desktop.config import CSS_DEFAULT_PATH, COLOR_PATH
import json


class DefaultStyle:
    """Rewrites the color.json with the default style"""

    def __init__(self, app):
        """Defines the constructor"""
        self.app = app

    def default_style(self):
        """Selects the default style"""
        with open(CSS_DEFAULT_PATH, 'r') as css_file:
            self.app.setStyleSheet(css_file.read())
        with open(COLOR_PATH, "w") as f:
            json.dump(CSS_DEFAULT_PATH, f)