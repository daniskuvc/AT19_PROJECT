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


import os
from dotenv import find_dotenv
from dotenv import set_key
from dotenv import dotenv_values
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
APP_SERVER='http://' + str(HOST_ML) + ':' + str(PORT_ML)
DOWNLOAD_DIR = APP_SERVER + '/download?file_name='

# print(envparams["HOST_ML"])
# print(UPLOAD_FOLDER)
# print(RESNET_MODEL_PATH)
