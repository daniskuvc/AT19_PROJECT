#
# @view_feature.py Copyright (c) 2023 Jalasoft.
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

class RunFeature(View):
    """Renders the feature page"""
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
        image_path = self.save_file(request.FILES['image'])
        uploaded_image_recognize = open(image_path, 'rb')

        files = {'image': uploaded_image_recognize}

        data = {'method': request.POST['method']}
        r = requests.post('http://localhost:5001/feature_recognizer', data = data, files = files)
        r = r.content.decode('utf-8')
        r = literal_eval(r)
        image_data = r['url']
        if 'age' in r['list'][0] or 'gender' in r['list'][0] or 'totalFaces' in r['list'][0]:
            return render(request, "feature.html", {'response': r, 'image': image_path, 'image_url' : image_data})
        else:
            result = []
            for item in r['list']:
                if 'emotion' in item:
                    emotion_dict = item["emotion"]
                    key, value = max(emotion_dict.items(), key = lambda item: item[1])
                    result.append({key:value})

                elif 'race' in item:
                    race_dict = item["race"]
                    key, value = max(race_dict.items(), key = lambda item: item[1])
                    result.append({key:value})
            return render(request, "feature.html", {'response': result, 'image': image_path, 'image_url' : image_data})

    def get(self, request):
        """Renders GET request"""
        return render(request, "feature.html")
