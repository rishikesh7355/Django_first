from django.shortcuts import render
#from django.conf import settings

# Create your views here.

def index(request):
    context = {}
        #"name":settings_DATA["NAME"],
        #"about_me":settings_DATA['ABOUT_ME']

    
    return render(request,'main/index.html',context)

def projects(request):
    context = {}
    return render(request,'main/projects.html',context)

def languages(request):
    context = {}
    return render(request,'main/languages.html',context)