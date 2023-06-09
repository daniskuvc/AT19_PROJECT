#
# @mongo_db.py Copyright (c) 2023 Jalasoft.
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

from factory_method.factory_method import FactoryMethod
from contract.i_repository import IRepository
from repository.mongo_db_repository import MongoDBRepository


class MongoDB(FactoryMethod):
    """Defines mongo_db creation."""
    
    def create_database(self) -> IRepository:
        """Defines the create_database method"""
        db = MongoDBRepository()
        return db
