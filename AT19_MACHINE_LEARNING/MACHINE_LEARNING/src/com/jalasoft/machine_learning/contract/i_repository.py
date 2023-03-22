#
# @i_repository.py Copyright (c) 2023 Jalasoft.
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

from zope.interface import Interface


class IRepository(Interface):
    """Class representing the interface."""   
    
    def db_connection(self):
        """Defines the contract db_connection"""
        pass

    def create(self, item, table_name):
        """Defines the contract create"""
        
        pass
    