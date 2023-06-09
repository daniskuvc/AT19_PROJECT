#
# @urls.py Copyright (c) 2023 Jalasoft.
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

"""project_frontend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from django.urls import include
from app.view_home import Home
from app.view_person import RunPerson
from app.view_feature import RunFeature
from app.view_logout import Logout



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home.as_view(), name = "home"),
    path('person/', RunPerson.as_view(), name = 'run_person'),
    path('feature/', RunFeature.as_view(), name = 'run_feature'),

    path("", include("allauth.urls")),
    path("logout", Logout.as_view()),
    path("person/logout", Logout.as_view()),
    path("feature/logout", Logout.as_view()),

]
