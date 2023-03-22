#
# @database_connection.py Copyright (c) 2023 Jalasoft.
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

import pymysql
from os import getenv
from config import MYSQLDB_HOST
from config import MYSQLDB_NAME
from config import MYSQLDB_PASS
from config import MYSQLDB_PORT
from config import MYSQLDB_USER


class DatabaseConnection:
    """Defines the connection to the database"""

    def __init__(self) -> None:
        self.db_host = MYSQLDB_HOST
        self.db_port = MYSQLDB_PORT
        self.db_user = MYSQLDB_USER
        self.db_pass = MYSQLDB_PASS
        self.db_name = MYSQLDB_NAME
        self.db_char = "utf8mb4"
        self.db_cursor = pymysql.cursors.DictCursor
        self.db_connection =''
        self.db_create_database()
        

    def db_connect(self):
        # print("xxxxxxxxxxxxx - Ejecute init", self.db_pass)
        connection = pymysql.connect(
            host=self.db_host,
            port=int(self.db_port),
            user=self.db_user,
            password=self.db_pass,
            db=self.db_name
        )
        return connection

    def db_return_connection(self):
        return self.db_connect
    
    def db_create_database(self):
        try:
            # print("xxxxxxxxxxxxx - Ejecute init", self.db_host)
            connection = pymysql.connect(
                host=self.db_host,
                port=int(self.db_port),
                user=self.db_user,
                password=self.db_pass)
 
            db_cursor = connection.cursor()
            db_cursor.execute("CREATE DATABASE IF NOT EXISTS `converter_db`;")
            db_cursor.close()
            
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("An error occurred while connecting: ", e)
        
    # try:
    #     cursor_instance = connection.cursor()
    #     sql_query = "CREATE DATABASE " + db_name
    #     cursor_instance.execute(sql_query)

    # except pymysql.err.OperationalError:
    #     raise Exception("No connection to the database.")

    # finally:
    #     connection.close()

            
#print("fck ------------------------", DatabaseConnection().db_connect().cursor())
