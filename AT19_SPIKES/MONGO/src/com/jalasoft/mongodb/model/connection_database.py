#
# @conection_database.py Copyright (c) 2022 Jalasoft.
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

from pymongo import MongoClient


class DatabaseConnection:
    """Defines the database connection"""
    def __init__(self, uri):
        self.uri = uri

    def db_connection(self):
        """Connects the database"""
        try:
            client = MongoClient(self.uri)
            db = client["db_users_app"]
        except ConnectionError:
            raise ConnectionError('Error connection with data base')
        return db
        