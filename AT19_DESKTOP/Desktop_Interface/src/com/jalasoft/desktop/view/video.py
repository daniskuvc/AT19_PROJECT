#
# @video.py Copyright (c) 2023 Jalasoft.
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

from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel, QLineEdit, QFileDialog, QPushButton, \
     QMessageBox, QAction, QMenu


class Video:
    """Defines the structure to choose the video to convert"""
    def __init__(self):
        """Defines the constructor"""
        self.init_video_label()
        self.init_video_path()
        self.file = QAction('Open file', triggered=self.open_file)
        self.url = QAction('Open URL', triggered=self.open_url)
        self.init_browse()

    def init_video_label(self):
        """Defines the labels"""
        self.label_video_path = QLabel()
        self.label_video_path.setText("Video Path:")
        self.label_video_path.setGeometry(18, 30, 80, 25)

    def get_video_label(self):
        """Returns the labels"""
        return self.label_video_path
    
    def init_video_path(self):
        """Creates the text box Video Path"""
        self.text_videopath = QLineEdit()
        self.text_videopath.setGeometry(93, 30, 175, 25)
        self.text_videopath.setObjectName("line_edit")

    def get_video_path(self):
        """Returns the text box Video Path"""
        return self.text_videopath

    def init_browse(self):
        """Creates the Browse button"""
        self.button_browse = QPushButton("Browse")
        self.button_browse.setGeometry(276, 30, 80, 25)
        self.button_browse.setObjectName("my_buttons")
        self.button_browse.clicked.connect(self.browse)
    
    def get_browse(self):
        """Returns the Browse button"""
        return self.button_browse

    def browse(self):
        """Captures the video path"""
        self.browse_menu = QMenu()
        self.browse_menu.addAction(self.file)
        self.browse_menu.addAction(self.url)
        self.browse_menu.exec_(QtGui.QCursor.pos())

    def open_file(self):
        """Opens the directory"""
        video_path, _ = QFileDialog.getOpenFileName(None, "Search file...", "C:\\",
                                                    "Wanted Files (*.mp4 *.mkv *.avi *.mpg)")
        self.text_videopath.setText(video_path)

    def open_url(self):
        """Displays an informational message"""
        QMessageBox.information(None, "Open URL", "Please paste an URL in the Video Path text field.", QMessageBox.Ok)
        self.text_videopath.setFocus()
        