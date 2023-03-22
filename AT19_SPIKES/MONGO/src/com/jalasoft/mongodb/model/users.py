#
# @users.py Copyright (c) 2022 Jalasoft.
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


class User:
    """Defines the user"""
    def __init__(self, name, age, country, user_name, email):
        self.name = name
        self.age = age
        self.country = country
        self.user_name = user_name
        self.email = email
    
    def toDBCollection(self):
        """Gives format for store in data base"""
        return{
            'name': self.name,
            'age': self.age,
            'country': self.country,
            'user_name': self.user_name,
            'email': self.email
        }
        