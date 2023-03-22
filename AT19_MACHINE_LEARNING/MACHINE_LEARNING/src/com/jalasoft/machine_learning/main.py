#
# @main.py Copyright (c) 2023 Jalasoft.
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
from flask_cors import CORS
from controler.routes import PersonRecognizer
from controler.routes import FeatureFaceRecognition
from controler.routes import ObjectRecognizer
from controler.routes import Download
from config import SWAGGER_URL
from config import SWAGGERUI_BLUEPRINT
from config import HOST_ML
from config import PORT_ML


app = Flask(__name__)
CORS(app)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
api = Api(app)
api.add_resource(FeatureFaceRecognition, '/feature_recognizer')
api.add_resource(PersonRecognizer, '/person_recognizer')
api.add_resource(ObjectRecognizer, '/object_recognizer')
api.add_resource(Download, '/download')

if __name__ == '__main__':
    app.run(debug = True, host=HOST_ML, port=PORT_ML)

