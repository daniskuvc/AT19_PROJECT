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

# Host, server, ports definitions
CONVERTER_HOST_ALL = envparams['CONVERTER_HOST_ALL']
CONVERTER_PORT = envparams['CONVERTER_PORT']
APP_SERVER = envparams['APP_SERVER']
DOWNLOAD_DIR = APP_SERVER + '/download?file_name='

MYSQLDB_HOST = envparams['MYSQLDB_HOST']
MYSQLDB_PORT = envparams['MYSQLDB_PORT']
MYSQLDB_USER = envparams['MYSQLDB_USER']
MYSQLDB_PASS = envparams['MYSQLDB_PASS']
MYSQLDB_NAME = envparams['MYSQLDB_NAME']
MYSQLDB_URI = envparams['MYSQLDB_URI']


SWAGGER_URL = '/converter'
API_URL = '/static/openapi.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Converter"
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
