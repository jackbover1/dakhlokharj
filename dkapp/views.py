from django.shortcuts import render
from django.conf.urls import url
from json import JSONEncoder
from datetime import *
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.

def submit_expense(request):
    this-token=request.POST['token']
