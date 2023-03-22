#
# @menu_bar.py Copyright (c) 2023 Jalasoft.
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

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QAction, QMenuBar, QMenu
from Desktop_Interface.src.com.jalasoft.desktop.view.menu_bar_about import About
from Desktop_Interface.src.com.jalasoft.desktop.view.menu_bar_color_style import ColorStyle
from Desktop_Interface.src.com.jalasoft.desktop.view.menu_bar_dark_style import DarkStyle
from Desktop_Interface.src.com.jalasoft.desktop.view.menu_bar_default_style import DefaultStyle
from Desktop_Interface.src.com.jalasoft.desktop.view.menu_bar_help import Help
from Desktop_Interface.src.com.jalasoft.desktop.view.menu_bar_open_url import OpenUrl
from Desktop_Interface.src.com.jalasoft.desktop.view.menu_bar_set_urls import SetUrls


class MenuBar(QMenuBar):
    """Creates the Menu bar"""
    set_video_path_action1_menu1 = pyqtSignal(str)

    def __init__(self, parent, app):
        """Defines the constructor"""
        super().__init__(parent)
        self.app = app
        self.setObjectName("line_menu")
        self.menu1 = QMenu("&File", self)
        self.addMenu(self.menu1)
        self.menu1_action1 = QAction('Open file', self)
        self.menu1_action1.triggered.connect(self.open_file)
        self.menu1.addAction(self.menu1_action1)
        self.menu1_action2 = QAction('Open URL', self)
        self.menu1_action2.triggered.connect(lambda: OpenUrl().open_url_option())
        self.menu1.addAction(self.menu1_action2)
        self.menu2 = QMenu("&Styles", self)
        self.addMenu(self.menu2)
        self.menu2_action1 = QAction('Dark', self)
        self.menu2_action1.triggered.connect(lambda: DarkStyle(self.app).dark_style())
        self.menu2.addAction(self.menu2_action1)
        self.menu2_action2 = QAction('Color', self)
        self.menu2_action2.triggered.connect(lambda: ColorStyle(self.app).color_style())
        self.menu2.addAction(self.menu2_action2)
        self.menu2_action3 = QAction('Default', self)
        self.menu2_action3.triggered.connect(lambda: DefaultStyle(self.app).default_style())
        self.menu2.addAction(self.menu2_action3)
        self.menu3 = QMenu("&Help", self)
        self.addMenu(self.menu3)
        self.menu3_action1 = QAction('Help', self)
        self.menu3_action1.triggered.connect(lambda: Help().help_option())
        self.menu3.addAction(self.menu3_action1)
        self.menu3_action2 = QAction('About', self)
        self.menu3_action2.triggered.connect(lambda: About().about_option())
        self.menu3.addAction(self.menu3_action2)
        self.menu4 = QMenu("&Settings", self)
        self.addMenu(self.menu4)
        self.menu4_action1 = QAction('Set URLs', self)
        self.menu4_action1.triggered.connect(lambda: SetUrls().popup_urls())
        self.menu4.addAction(self.menu4_action1)
    
    def open_file(self):
        """Opens the directory"""
        video_path, _ = QFileDialog.getOpenFileName(None, "Search file...", "C:\\",
                                                    "Wanted Files (*.mp4 *.mkv *.avi *.mpg)")
        self.set_video_path_action1_menu1.emit(video_path)