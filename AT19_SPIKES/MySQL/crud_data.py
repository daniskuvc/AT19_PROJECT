#
# @crud_data.py Copyright (c) 2022 Jalasoft.
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


from database_connection import DatabaseConnection as db

mycursor = db.connection.cursor()


class CreateTable:
    """Defines Create table function"""

    def create_table():
        """Creates a table"""
    
        mycursor.execute("CREATE TABLE person (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), email VARCHAR(50), age INT)")
        print("Table created")
        db.connection.close()


class CRUD:
    """"Defines Create, Read, Update and Delete functions"""
    
    def insert_data(name, email, age):
        """Inserts data"""
      
        query = "INSERT INTO person (name, email, age) VALUES (%s, %s, %s)"    
        mycursor.execute(query, (name,email,age))
        print("Data inserted")
        db.connection.close()
    
    def read_all_data():
        """Reads all data"""
    
        query = "SELECT name, email, age FROM person"
        mycursor.execute(query)
        datos = mycursor.fetchall()
        for dato in datos:
            print(dato)
        print("Data read")
        db.connection.close()

    def read_specific_data(name):
        """Reads data searching by its name"""
    
        query = "SELECT name, email, age FROM person WHERE name = %s"    
        mycursor.execute(query,(name))
        datos = mycursor.fetchall()
        for dato in datos:
            print(dato)
        print("Data read")
        db.connection.close()

    def update_data(newName,id):
        """Updates data"""
    
        query = "UPDATE person SET name = %s  WHERE id = %s"
        mycursor.execute(query, (newName, id))
        print("Data updated")
        db.connection.close()


    def delete_data(id):
        """Deletes data"""
    
        query = "DELETE FROM person WHERE id = %s"
        mycursor.execute(query, (id))
        print("Data deleted")
        db.connection.close()
