#
# @main.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from flask import Flask
from routes.auth import routes_auth
from dotenv import load_dotenv

app = Flask(__name__)

app.register_blueprint(routes_auth, url_prefix = "/api")

if __name__ == '__main__':
    load_dotenv()
    app.run(debug = True, port = "4000", host = "0.0.0.0")