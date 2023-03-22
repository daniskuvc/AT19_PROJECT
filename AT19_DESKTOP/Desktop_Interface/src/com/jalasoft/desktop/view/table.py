#
# @table.py Copyright (c) 2023 Jalasoft.
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

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView


class Table:
    """Defines the structure of table"""
    def __init__(self):
        """Defines the constructor"""
        self.init_ui_table()
    
    def init_ui_table(self):
        """Creates the table"""
        self.result_table = QTableWidget()
        self.result_table.setObjectName("table")
        self.result_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.result_table.setDragDropOverwriteMode(False)
        self.result_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.result_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.result_table.setTextElideMode(Qt.ElideRight)
        self.result_table.setWordWrap(False)
        self.result_table.setSortingEnabled(False)
        self.result_table.setColumnCount(5)
        self.result_table.setRowCount(0)
        self.result_table.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter | Qt.AlignCenter)
        self.result_table.horizontalHeader().setHighlightSections(False)
        self.result_table.horizontalHeader().setStretchLastSection(True)
        self.result_table.verticalHeader().setVisible(False)
        self.result_table.verticalHeader().setDefaultSectionSize(20)
        self.result_table.setRowCount(25)
        name_columns = ("File", "Time (seconds)", "Percentage (%)","Word", "Algorithm")
        self.result_table.setHorizontalHeaderLabels(name_columns)

        for indice, ancho in enumerate((230, 230, 230, 230, 230), start=0):
            self.result_table.setColumnWidth(indice, ancho)

        self.result_table.setGeometry(10, 72, 1180, 550)

    def get_result_table(self):
        """Returns the table"""
        return self.result_table

    def set_result_table(self, data):
        """Set values to the table"""
        self.result_table.setRowCount(len(data))
        for row, element in enumerate(data):
            self.result_table.setItem(row, 0, QTableWidgetItem(element['file_name']))
            self.result_table.setItem(row, 1, QTableWidgetItem(element['second']))
            self.result_table.setItem(row, 2, QTableWidgetItem(element['percentage']))
            self.result_table.setItem(row, 3, QTableWidgetItem(element['word']))
            self.result_table.setItem(row, 4, QTableWidgetItem(element['model']))  
