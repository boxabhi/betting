from django.shortcuts import render,HttpResponse
from api.utility.cricket_api import get_cricket_data
from api.models import cricketApi
from django.http import JsonResponse
# Create your views here.
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def home(request):
    return Response({"string" :"Yes Django!"})

@api_view(['GET'])
def show_response(request):
    data = cricketApi.objects.all()
    d = json.loads(data[0].data)
    return Response(d['matches'])

def request_api(request):
    get_cricket_data()
    return HttpResponse("<h1>Hello Django!</h1>")