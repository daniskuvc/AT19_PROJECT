#
# @main_window.py Copyright (c) 2023 Jalasoft.
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
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton, QDialog, QMessageBox
from Desktop_Interface.src.com.jalasoft.desktop.view.results_data import Results
from Desktop_Interface.src.com.jalasoft.desktop.controller.converter import Converter
from Desktop_Interface.src.com.jalasoft.desktop.controller.machine_learning import MachineLearning
from Desktop_Interface.src.com.jalasoft.desktop.view.table import Table
from Desktop_Interface.src.com.jalasoft.desktop.view.video import Video
from Desktop_Interface.src.com.jalasoft.desktop.view.word import Word
from Desktop_Interface.src.com.jalasoft.desktop.view.model import Model
from Desktop_Interface.src.com.jalasoft.desktop.view.percentage import SetPer
from Desktop_Interface.src.com.jalasoft.desktop.view.output_format import OutputFormat
from Desktop_Interface.src.com.jalasoft.desktop.view.menu_bar import MenuBar
from Desktop_Interface.src.com.jalasoft.desktop.view.new_search import NewSearch
from Desktop_Interface.src.com.jalasoft.desktop.common.validate import ValidateInput
from Desktop_Interface.src.com.jalasoft.desktop.common.response_validator import ValidateResponse
from Desktop_Interface.src.com.jalasoft.desktop.common.exception.pyqt_exception import PyqtException
import os
from Desktop_Interface.src.com.jalasoft.desktop.config import IMG_ICON_PATH


class Window(QMainWindow):
    """Defines the UI"""

    def __init__(self, app):
        """Defines the constructor and window"""
        super().__init__()
        self.app = app
        self.main_window()
        self.menu_bar = MenuBar(self, self.app)
        self.create_menus()
        self.result_video = Video()
        self.video_path_set()
        self.result_word = Word()
        self.word_set()
        self.result_percentage = SetPer()
        self.percentage_set()
        self.result_output_format = OutputFormat()
        self.output_format_set()
        self.result_model = Model()
        self.combo_model_set()
        self.result_table_body = Table()
        self.result_table_set()
        self.result_new_search = NewSearch()
        self.ui_components()
        self.show()
        
    def main_window(self):
        """Creates the main window"""
        self.setWindowIcon(QtGui.QIcon(IMG_ICON_PATH))
        self.setWindowTitle("Convert and Recognition Studio")
        self.setObjectName("mainwindow")
        self.setFixedSize(QSize(1200, 700))

    def create_menus(self):
        """Creates the menu"""
        self.setMenuBar(self.menu_bar)
        self.menu_bar.set_video_path_action1_menu1.connect(self.set_line_edit_text_action1_menu1)

    def video_path_set(self):
        """Creates the lineEdit and button of the Video Path"""
        self.label_video_path = self.result_video.get_video_label()
        self.label_video_path.setParent(self)

        self.text_videopath = self.result_video.get_video_path()
        self.text_videopath.setParent(self)

        self.button_browse = self.result_video.get_browse()
        self.button_browse.setParent(self)

    def word_set(self):
        """Creates the lineEdit of the Word"""
        self.label_word = self.result_word.get_word_label()
        self.label_word.setParent(self)

        self.text_word = self.result_word.get_word_line()
        self.text_word.setParent(self)

    def combo_model_set(self):
        """Creates the comboBox of the Neural Model"""
        self.label_model = self.result_model.get_model_label()
        self.label_model.setParent(self)

        self.combo_model = self.result_model.get_model_combo()
        self.combo_model.setParent(self)

    def percentage_set(self):
        """Creates the lineEdit of the Percentage"""
        self.label_percentage = self.result_percentage.get_percentage_label()
        self.label_percentage.setParent(self)

        self.text_percentage = self.result_percentage.get_text_percentage()
        self.text_percentage.setParent(self)

    def output_format_set(self):
        """Creates the comboBox of the Output Format"""
        self.label_format = self.result_output_format.get_format_label()
        self.label_format.setParent(self)

        self.combo_format = self.result_output_format.get_format_combo()
        self.combo_format.setParent(self)

    def result_table_set(self):
        """Creates the table"""
        self.result_table = self.result_table_body.get_result_table()
        self.result_table.setParent(self)

    def ui_components(self):
        """Defines all the compenents the UI"""
        button_show_Image = QPushButton("Show Image", self)
        button_show_Image.setGeometry(1030, 640, 150, 25)
        button_show_Image.setObjectName("my_buttons")
        button_show_Image.clicked.connect(self.button_show_image)

        button_download_Image = QPushButton("Download Image", self)
        button_download_Image.setGeometry(870, 640, 150, 25)
        button_download_Image.setObjectName("my_buttons")
        button_download_Image.clicked.connect(self.download_image)

        button_search = QPushButton("Search", self)
        button_search.setGeometry(1024, 30, 80, 25)  
        button_search.setObjectName("my_buttons")
        button_search.clicked.connect(lambda: self.search(self.text_videopath.text(), self.text_word.text(),
                                                          self.text_percentage.text(), self.combo_format.currentText(),
                                                          self.combo_model.currentText()))

        self.button_new_search = self.result_new_search.get_init_button()
        self.button_new_search.setParent(self)
        self.result_new_search.action_to_click.connect(self.clean)
    
    def set_line_edit_text_action1_menu1(self, text):
        """Get menu signal"""
        self.text_videopath.setText(text)

    def search(self, video_path, word, percentage, combo_format, combo_model):
        """Gets input information and completes the table with data"""
        try:
            ValidateInput().validate_video_path(video_path)
            ValidateInput().validate_word(word)
            ValidateInput().validate_percentage(percentage)
            zip_to_send_machine, code_converter = Converter().get_zip(combo_format, video_path)
            ValidateResponse().validate_status_code_response(code_converter)
            machine_result, code_machine = MachineLearning().send_zip(int(percentage), combo_model, word, zip_to_send_machine)
            ValidateResponse().validate_status_code_response(code_machine)
            result_link = machine_result.get('url')
            fill_table = machine_result.get('list')
            ValidateResponse().validate_machine_learning_response(fill_table)
            self.path_image_folder, code_machine_zip = MachineLearning().get_zip(result_link)
            ValidateResponse().validate_status_code_response(code_machine_zip)
            self.data = Results(fill_table, word, combo_model).results()
            self.result_table_body.set_result_table(self.data)
        except PyqtException as error:
            error_popup = QMessageBox()
            error_popup.setWindowTitle("Error")
            error_popup.setText(error.get_message())
            error_popup.setWindowIcon(QIcon(IMG_ICON_PATH))
            error_popup.exec_()

    def clean(self):
        """Deletes data"""
        self.text_word.setText('')
        self.text_videopath.setText('')
        self.text_percentage.setText('')
        self.result_table.clearContents()
        self.result_table.setRowCount(0)

    def button_show_image(self):
        """Opens the popup window with the selected photo"""
        row_selected = self.result_table.selectedItems()
        if row_selected:
            image = self.data[row_selected[0].row()]['file_name']
            path = self.path_image_folder
            self.popup_show_image(os.path.join(path, image))
        else:
            QMessageBox.information(self, "Image", "Select a row.", QMessageBox.Ok)

    def popup_show_image(self, image):
        """ Creates the popup window"""
        popup = QDialog()
        popup.setWindowTitle('Image preview')
        popup.setWindowIcon(QtGui.QIcon(IMG_ICON_PATH))
        lbl_popup = QLabel(popup)
        pixmap = QPixmap(image)
        lbl_popup.setPixmap(pixmap)
        lbl_popup.resize(pixmap.width(), pixmap.height())
        popup.exec_()

    def download_image(self):
        """Downloads the selected image"""
        row_selected = self.result_table.selectedItems()
        if row_selected:
            image = self.data[row_selected[0].row()]['file_name']
        else:
            QMessageBox.information(self, "Image", "Select a row.", QMessageBox.Ok)
