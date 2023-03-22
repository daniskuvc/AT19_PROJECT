#
# @word.py Copyright (c) 2023 Jalasoft.
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


class Word:
    """Defines the structure to type the word to search"""
    def __init__(self):
        """Defines the constructor"""
        self.init_word_label()
        self.init_word_line()

    def init_word_label(self):
        """Defines the labels"""
        self.label_word = QLabel()
        self.label_word.setText("Word:")
        self.label_word.setGeometry(364, 30, 40, 25)

    def get_word_label(self):
        """Returns the labels"""
        return self.label_word

    def init_word_line(self):
        """Creates the text box word"""
        self.text_word = QLineEdit()
        self.text_word.setGeometry(404, 30, 150, 25)
        self.text_word.setObjectName("line_edit")

    def get_word_line(self):
        """Returns the text box word"""
        return self.text_word
        