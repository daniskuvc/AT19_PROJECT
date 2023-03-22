#
# @config.py Copyright (c) 2023 Jalasoft.
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


PATH = os.path.realpath(os.path.dirname(__file__))
CSS_PATH = os.path.join(PATH, 'styles')
IMG_PATH = os.path.join(PATH, 'static')
DATA_PATH = os.path.join(IMG_PATH, 'data.json')
COLOR_PATH = os.path.join(IMG_PATH, 'color.json')
IMG_ICON_PATH = os.path.join(IMG_PATH, 'icon.png')
CSS_DARK_PATH = os.path.join(CSS_PATH, 'dark_style.css')
CSS_COLOR_PATH = os.path.join(CSS_PATH, 'color_style.css')
CSS_DEFAULT_PATH = os.path.join(CSS_PATH, 'default_style.css')
