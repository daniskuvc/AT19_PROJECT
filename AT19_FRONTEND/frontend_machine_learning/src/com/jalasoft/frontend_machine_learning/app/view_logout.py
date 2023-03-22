#
# @view_logout.py Copyright (c) 2023 Jalasoft.
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


from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views import View


class Logout(View):
    """Renders the log out page"""
    def get(self, request):
        """Renders GET request"""
        logout(request)
        return redirect("/")