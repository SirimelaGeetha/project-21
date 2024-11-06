from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def insert_topic(request):
    ETMFO=TopicModelForm()
    d={'ETMFO':ETMFO }
    if request.method=='POST':
        TMFDO=TopicModelForm(request.POST)
        if TMFDO.is_valid():
            TMFDO.save()
            return HttpResponse('created')
        else:
            return HttpResponse('invalid')
    return render(request,'insert_topic.html',d)
def insert_webpage(request):
    EWMFO=WebpageModelForm()
    d={'EWMFO':EWMFO}
    if request.method=='POST':
        WMFDO=WebpageModelForm(request.POST)
        if WMFDO.is_valid():
            WMFDO.save()
            return HttpResponse('created')
        else:
            return HttpResponse('invalid')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    EARMFO=AccessRecordModelForm()
    d={'EARMFO':EARMFO}
    if request.method=='POST':
        ARMFDO=AccessRecordModelForm(request.POST)
        if ARMFDO.is_valid():
            ARMFDO.save()
            return HttpResponse('created')
        else:
            return HttpResponse('invalid')
    return render(request,'insert_accessrecord.html',d)


def wish(request,name):
    return HttpResponse(f'<h1> Hello {name} How r u</h1>')
   

            
    

       