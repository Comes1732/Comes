import json
from django.shortcuts import render

# Create your views here.

from django.views import View
from django.http import HttpResponse,JsonResponse

class UtilTestViews(View):
    def get(self, request):
        data = {'code': 200, 'msg': 'successful'}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')
