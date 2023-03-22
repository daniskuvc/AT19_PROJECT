#
# @login_crud.py Copyright (c) 2023 Jalasoft.
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

from os import getenv
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import MYSQLDB_HOST
from config import MYSQLDB_NAME
from config import MYSQLDB_PASS
from config import MYSQLDB_PORT
from config import MYSQLDB_USER
from config import MYSQLDB_URI


Base = declarative_base()
db_user = MYSQLDB_USER
db_password = MYSQLDB_PASS
db_host = MYSQLDB_HOST
db_port = MYSQLDB_PORT
db_name = MYSQLDB_NAME


class User(Base):
    """Defines user table"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), unique=True, nullable=False)
    password = Column(String(80), nullable=False)


engine = create_engine(MYSQLDB_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class UserCRUD():
    """Process CRUD"""
    def create(self):
        user_name = "converter_user"
        password = "1234"
        existing_user = session.query(User).filter_by(user_name= user_name).first()
        if not existing_user:
            user = User(user_name= user_name, password= password)
            session.add(user)
            session.commit()

    def read(self, username):
        """Reads from data base"""
        user = session.query(User).filter_by(user_name= username).first()
        return user
