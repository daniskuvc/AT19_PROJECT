#
# @new_search.py Copyright (c) 2023 Jalasoft.
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
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QPushButton


class NewSearch(QObject):
    """Defines the structure """
    action_to_click = pyqtSignal()

    def __init__(self):
        """Defines the constructor"""
        super().__init__()
        self.init_button()

    def init_button(self):
        """Creates the New search button"""
        self.new_search = QPushButton("New search")
        self.new_search.setGeometry(1110, 30, 80, 25)
        self.new_search.setObjectName("my_buttons")
        self.new_search.clicked.connect(self.emit_signal)

    def get_init_button(self):
        """Returns the New search button"""
        return self.new_search

    def emit_signal(self):
        """Emits the signal"""
        self.action_to_click.emit()
