#
# @model.py Copyright (c) 2023 Jalasoft.
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


class Model:
    """Defines the structure to choose the model to use"""
    def __init__(self):
        """Defines the constructor"""
        self.init_model_label()
        self.init_model_combo()

    def init_model_label(self):
        """Defines the labels"""
        self.label_model = QLabel()
        self.label_model.setText("Neural Model:")
        self.label_model.setGeometry(830, 30, 100, 25)

    def get_model_label(self):
        """Returns the labels"""
        return self.label_model
        
    def init_model_combo(self):
        """Defines the combo model"""
        self.combo_model = QComboBox()
        self.combo_model.setGeometry(912, 30, 100, 25)
        self.combo_model.addItem("resnet")
        self.combo_model.addItem("inception")
        self.combo_model.addItem("desnet")
        self.combo_model.addItem("mobile")
        self.combo_model.setObjectName("comboBox")
        
    def get_model_combo(self):
        """Returns the combo model"""
        return self.combo_model
        