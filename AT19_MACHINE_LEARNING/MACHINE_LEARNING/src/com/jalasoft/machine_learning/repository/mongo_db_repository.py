#
# @mongo_db_repository.py Copyright (c) 2023 Jalasoft.
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
from typing import TypeVar
from typing import Generic
from contract.i_repository import IRepository
from config import MONGODB_URI
import os
import zope.interface

T = TypeVar('T')
# URI = os.getenv('URI')


@zope.interface.implementer(IRepository)
class MongoDBRepository(Generic[T]):
    """Defines the database connection."""
    def __init__(self):
        """Defines the init""" 
        self.uri = MONGODB_URI

    def db_connection(self):
        """Connects the database"""
        try:
            client = MongoClient(self.uri)
            db = client["db_app"]
        except ConnectionError:
            raise ConnectionError('Error connection with data base')
        return db

    def create(self, item, table_name):
        """Defines the create method"""
        db = self.db_connection()
        collection = db[table_name]
        collection.insert_one(item.toDBCollection())
