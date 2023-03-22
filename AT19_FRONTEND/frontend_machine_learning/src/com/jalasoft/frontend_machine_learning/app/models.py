#
# @models.py Copyright (c) 2023 Jalasoft.
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

from django.db import models


class Document(models.Model):
    """Defines Models"""
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="Uploaded_Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)

