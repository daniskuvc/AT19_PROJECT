#
# @auth.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from flask import Blueprint
from flask import jsonify
from flask import request
from function_jwt import write_token
from function_jwt import validate_token


routes_auth = Blueprint("routes_auth", __name__)


@routes_auth.route("/login", methods = ["POST"])
def login():
    """Simulates login and generates the token"""

    data = request.get_json()
    if data['username'] == "Carolina Vacaflor":
        return write_token(data=request.get_json())
    else:
        response = jsonify({"message": "User not found"})
        response.status_code = 404
        return response

@routes_auth.route("/verify/token")
def verify():
    """Verifies if the token is valid"""

    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=True)