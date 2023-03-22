#
# @menu_bar_set_urls.py Copyright (c) 2023 Jalasoft.
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
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QGridLayout
from Desktop_Interface.src.com.jalasoft.desktop.config import IMG_ICON_PATH, DATA_PATH
from Desktop_Interface.src.com.jalasoft.desktop.view.submit import SubmitButton
import json


class SetUrls:
    """Creates the Set URLs popup"""
    def popup_urls(self):
        """Shows a window to set URLs"""
        url_popup = QDialog()
        url_popup.setWindowTitle("URL Settings")
        url_popup.setWindowIcon(QIcon(IMG_ICON_PATH))

        label1 = QLabel("Converter URL:")
        label2 = QLabel("Machine Learning URL:")
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
        self.textbox1 = QLineEdit(data["converter"])
        self.textbox1.setObjectName("line_edit")
        self.textbox2 = QLineEdit(data["machine learning"])
        self.textbox2.setObjectName("line_edit")
        button_submit = QPushButton("Submit")
        button_submit.setObjectName("my_buttons")
        button_submit.clicked.connect(lambda: SubmitButton().submit(self.textbox1.text(), self.textbox2.text()))
        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.textbox1, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.textbox2, 1, 1)
        layout.addWidget(button_submit, 2, 1)
        url_popup.setLayout(layout)
        url_popup.setGeometry(700, 400, 500, 300)
        url_popup.exec_()