from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pydicom


# Create your views here.

def hello(request):
   
    return HttpResponse('gg')



def index(request):
    im = pydicom.read_file('case3a_001.dcm')

    name = im['PatientName']

    title = name 
    return  render(request, 'index.html',{
        'tittle' : title
    })