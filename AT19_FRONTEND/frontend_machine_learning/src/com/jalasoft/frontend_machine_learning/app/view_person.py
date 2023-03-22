#
# @view_person.py Copyright (c) 2023 Jalasoft.
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

from django.shortcuts import render
from django.views import View
from ast import literal_eval
from app.models import Document
import os
import requests


MEDIA_PATH = os.path.realpath(os.path.dirname(__file__))
FILE_MEDIA_PATH = os.path.join(MEDIA_PATH, '../media/Uploaded_Files')

class RunPerson(View):
    """Renders the person page"""
    def save_file(self, file_to_save):
        """Stores the file locally"""
        document = Document(
            title = str(file_to_save),
            uploadedFile = file_to_save
        )
        document.save()
        return os.path.join(FILE_MEDIA_PATH, str(file_to_save))

    def post(self, request):
        """Renders the response POST requests"""
        known_image_path = self.save_file(request.FILES['known_image'])
        uploaded_known_image = open(known_image_path, 'rb')
        unknown_image_path = self.save_file(request.FILES['unknown_image'])
        uploaded_unknown_image = open(unknown_image_path, 'rb')

        files = {
            'known_image': uploaded_known_image,
            'unknown_image': uploaded_unknown_image
        }

        r = requests.post('http://0.0.0.0:5001/person_recognizer', 
                        data = {'known_name': request.POST['known_name']}, files = files)
        r = r.content.decode('utf-8')
        r = literal_eval(r)
        print(r)
        image_data = r['url']
        return render(request, "person.html",
                      {'response': r, 'known_image': known_image_path, 'unkown_image': unknown_image_path,
                       'image_url' : image_data})

    def get(self, request):
        """Renders GET request"""
        return render(request, "person.html")
   