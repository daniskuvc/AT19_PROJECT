#
# @main.py Copyright (c) 2022 Jalasoft.
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

from flask import Flask
from flask_restful import Api
from db_controller.crud_users import ShowUsers
from db_controller.crud_users import CreateUser
from db_controller.crud_users import FindUser
from db_controller.crud_users import DeleteUser
from db_controller.crud_users import UpdateUser

app = Flask(__name__)
api = Api(app)
api.add_resource(CreateUser, '/create_users')
api.add_resource(ShowUsers, '/show_all_users')
api.add_resource(FindUser, '/find_user/<string:user_name>')
api.add_resource(DeleteUser, '/delete/<string:user_name>')
api.add_resource(UpdateUser, '/update/<string:user_name>')

if __name__ == '__main__':
    app.run(debug=True, port=4000)
