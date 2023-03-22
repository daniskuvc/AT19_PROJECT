#
# @crud_users.py Copyright (c) 2022 Jalasoft.
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

from flask import request
from flask_restful import Resource
from model.connection_database import DatabaseConnection
from model.users import User
from dotenv import load_dotenv
import os
import json

load_dotenv()
URI = os.getenv('URI')
db = DatabaseConnection(URI).db_connection()



def get_form_information(request):
    """Gets the data from the form"""
    name = request.form['name']
    age = request.form['age']
    country = request.form['country']
    user_name = request.form['user_name']
    email = request.form['email']
    return {
            'name': name,
            'age': age,
            'country': country,
            'user_name': user_name,
            'email': email
            }


class CreateUser(Resource):
    """Defines Create User class"""
    def post(self):
        """Creates a user"""
        users = db['users']
        get_user = get_form_information(request)
        if (get_user['name'] and get_user["age"] and get_user["country"]
                and get_user["user_name"] and get_user["email"]):
            user = User(get_user['name'], get_user["age"], get_user["country"], get_user["user_name"],
                        get_user["email"])
            find_email = users.find_one({'email': user.email})
            find_user_name = users.find_one({'user_name': user.user_name})
            if find_email:
                return 'email already used'
            elif find_user_name:
                return 'user already exist'
            else:
                users.insert_one(user.toDBCollection())
                response = {
                            'name': get_user['name'],
                            'age': get_user["age"],
                            'country': get_user["country"],
                            'user_name': get_user["user_name"],
                            'email': get_user["email"]
                            }
                response = json.dumps(response)
                print(response)
                return response, 200


class ShowUsers(Resource):
    """Defines Show Users class"""
    def get(self):
        """Show all the users"""
        users = db['users']
        users = users.find({})
        list_users = []
        for user in users:
            list_users.append({
                            'name': user['name'],
                            'age': user['age'],
                            'country': user['country'],
                            'user_name': user['user_name'],
                            'email': user['email']
                            })
        return json.dumps(list_users), 200


class FindUser(Resource):
    """Defines Find User class"""
    def get(self, user_name):
        """Finds an user"""
        users = db['users']
        users = users.find({'user_name': user_name})
        list_users = []
        for user in users:
            list_users.append({
                            'name': user['name'],
                            'age': user['age'],
                            'country': user['country'],
                            'user_name': user['user_name'],
                            'email': user['email']
                             })
        if len(list_users) == 0:
            return 'User not found'
        return json.dumps(list_users), 200


class DeleteUser(Resource):
    """Defines Delete User class"""
    def delete(self, user_name):
        """Deletes an user"""
        users = db['users']
        users.delete_one({'user_name': user_name})
        response = json.dumps({'message': f'User {user_name} deleted'})
        return response


class UpdateUser(Resource):
    """Defines Update User class"""
    def put(self, user_name):
        """Updates a user"""
        users = db['users']
        get_user = get_form_information(request)
        if get_user['name'] and get_user["age"] and get_user["country"] and get_user["user_name"] and get_user["email"]:
            users.update_one({'user_name': user_name},
                            {'$set': {'name': get_user['name'],
                            "age": get_user["age"],
                            "country": get_user["country"],
                            "user_name": get_user["user_name"],
                            "email": get_user["email"]}})
            response = json.dumps({'messege': f'User {user_name} updated'})
            return response
