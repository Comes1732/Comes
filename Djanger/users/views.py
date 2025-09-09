# -*- coding: utf-8 -*-
"""
User-related Views
Functional Description: Implements the core logic for processing user-related information workflows
Creation Date: 2025-09-09
Last Modified: 2025-09-09
Author: Zhan Cui
Copyright Notice: © 2025 Company Name. All rights reserved.
"""
import json
from django.views import View
from django.http import HttpResponse

class UtilTestViews(View):
    def get(self, request):
        data = {'code': 200, 'msg': 'successful'}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')

    
    def post(self, request):
        return HttpResponse("User Profile Updated (POST)")
    




class UtilTestViews(View):
    def get(self, request):
        data = {'code': 200, 'msg': 'successful'}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')
