#
# @config.py Copyright (c) 2023 Jalasoft.
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


import os
import json
from flask import request
from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import find_dotenv
from dotenv import set_key
from dotenv import dotenv_values
# from dotenv import load_dotenv
# load_dotenv()

# Get and set environment info
envfile_path = find_dotenv()
set_key(envfile_path, "ROOT_PATH", os.path.dirname(envfile_path))
envparams = dotenv_values()

# Paths definitions
UPLOAD_FOLDER = envparams["UPLOAD_FOLDER"]
RESPONSE_FOLDER = envparams["RESPONSE_FOLDER"]
os.makedirs(str(UPLOAD_FOLDER), exist_ok=True)
os.makedirs(str(RESPONSE_FOLDER), exist_ok=True)

RESNET_MODEL_PATH = envparams["RESNET_MODEL_PATH"]
DESNET_MODEL_PATH = envparams["DESNET_MODEL_PATH"]
INCEPTION_MODEL_PATH = envparams["INCEPTION_MODEL_PATH"]
MOBILE_MODEL_PATH = envparams["MOBILE_MODEL_PATH"]
CASC_PATH = envparams["CASC_PATH"]

# Host, server, ports definitions
HOST_ML = envparams['HOST_ML']
PORT_ML = envparams['PORT_ML']
APP_SERVER=envparams['APP_SERVER']
DOWNLOAD_DIR = APP_SERVER + '/download?file_name='

MONGODB_URI="mongodb://" + envparams['MONGODB_USER'] + ":" + envparams['MONGODB_PASS'] + "@" + \
    envparams['MONGODB_HOST'] + ":" + envparams['MONGODB_PORT']

SWAGGER_URL = '/ML'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Recognizer"
    }
)

def swagger_update_server():
    swagger_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), API_URL[1:])
    jsonFile = open(swagger_path, "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file

    ## Working with buffered content
    data["servers"][0]["url"] = str(APP_SERVER)

    ## Save our changes to JSON file
    jsonFile = open(swagger_path, "w+")
    jsonFile.write(json.dumps(data, indent=2))
    jsonFile.close()

# swagger_update_server()
