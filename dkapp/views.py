from django.shortcuts import render
from django.conf.urls import url
from json import JSONEncoder
from datetime import *
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404,render
from .models import Token,Kharj,Dakhl

# Create your views here.

@csrf_exempt


def sabte_kharj(request):
    in_tarikh=request.POST['tarikh'] if 'tarikh' in request.POST else timezone.now()
    in_tozih=request.POST['tozih'] if 'tozih' in request.POST else ""
    in_mablagh=request.POST['mablagh'] if 'mablagh' in request.POST else "0"
    in_token=request.POST['token'] if 'token' in request.POST else ""
    in_nam=get_object_or_404(User,token__token=in_token)
    Kharj.objects.create(nam=in_nam,mablagh=in_mablagh,tozih=in_tozih,tarikh=in_tarikh)
    return JsonResponse({
      'sabt':'shod'
    },encoder=JSONEncoder)
@csrf_exempt
def sabte_dakhl(request):
  in_tarikh=request.POST['tarikh'] if 'tarikh' in request.POST else timezone.now()
  in_tozih=request.POST['tozih'] if 'tozih' in request.POST else ""
  in_mablagh=request.POST['mablagh'] if 'mablagh' in request.POST else "0"
  in_token=request.POST['token'] if 'token' in request.POST else ""
  in_nam=get_object_or_404(User,token__token=in_token)
  Kharj.objects.create(nam=in_nam,mablagh=in_mablagh,tozih=in_tozih,tarikh=in_tarikh)
  return JsonResponse({
    'sabt':'shod'
  },encoder=JSONEncoder)