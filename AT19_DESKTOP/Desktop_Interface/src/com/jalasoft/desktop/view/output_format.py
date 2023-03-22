#
# @output_format.py Copyright (c) 2023 Jalasoft.
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

from PyQt5.QtWidgets import QLabel, QComboBox


class OutputFormat:
    """Defines the structure to choose the output format"""
    def __init__(self):
        """Defines the constructor"""
        self.init_format_label()
        self.init_format_combo()

    def init_format_label(self):
        """Defines the labels"""
        self.label_format = QLabel()
        self.label_format.setText("Output Format:")
        self.label_format.setGeometry(664, 30, 105, 25)

    def get_format_label(self):
        """Returns the labels"""
        return self.label_format

    def init_format_combo(self):
        """Defines the combo model"""
        self.combo_format = QComboBox()
        self.combo_format.setGeometry(755, 30, 70, 25)
        self.combo_format.addItem("jpg")
        self.combo_format.addItem("png")
        self.combo_format.setObjectName("comboBox")
    
    def get_format_combo(self):
        """Returns the combo model"""
        return self.combo_format
