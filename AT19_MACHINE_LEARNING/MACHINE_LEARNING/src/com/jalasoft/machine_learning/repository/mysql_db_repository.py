#
# @mysql_db_repository.py Copyright (c) 2023 Jalasoft.
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

from typing import TypeVar
from typing import Generic
from contract.i_repository import IRepository
import os
import zope.interface

T = TypeVar('T')
URI = os.getenv('URI')


@zope.interface.implementer(IRepository)
class MySQLRepository(Generic[T]):
    """Defines the database connection."""
    def __init__(self):
        """Defines the init""" 
        pass

    def db_connection(self):
        """Connects the database"""
        pass

    def create(self, item: T, table_name):
        """Defines the create method"""
        pass
