#
# @percentage.py Copyright (c) 2023 Jalasoft.
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

from PyQt5.QtWidgets import QLabel, QLineEdit


class SetPer:
    """Defines the structure to text box percentage"""
    def __init__(self):
        """Defines the constructor"""
        self.init_percentage_label()
        self.init_percentage_line()

    def init_percentage_label(self):
        """Defines the labels"""
        self.label_percentage = QLabel()
        self.label_percentage.setText("Per. %")
        self.label_percentage.setGeometry(562, 30, 45, 25)
    
    def get_percentage_label(self):
        """Returns the labels"""
        return self.label_percentage
    
    def init_percentage_line(self):
        """Defines the text box to write the percentage"""
        self.text_percentage = QLineEdit()
        self.text_percentage.setGeometry(607, 30, 50, 25)
        self.text_percentage.setObjectName("line_edit")

    def get_text_percentage(self):
        """Return the percentage text box"""
        return self.text_percentage
