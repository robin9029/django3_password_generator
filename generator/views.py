from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
thepassword1= ''
def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def youtube(request):
    #return render(request,'generator/youtube.html')
    print('thepassword2: ',thepassword1)
    return render(request,'generator/youtube.html',{'title':thepassword1,'link':'http://youtube.com+thepassword1'})


def password(request):
    characters= list('abcdefghijklmnopqrstuvwxyz')
    print('request: ',request)
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length',12))
    thepassword= ''
    #print('characters: ',characters)
    for x in range(length):
        thepassword += random.choice(characters)
    #print('thepassword: ',thepassword)
    thepassword1=thepassword
    print('thepassword: ',thepassword1)
    return render(request,'generator/password.html',{'password':thepassword})
