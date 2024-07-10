from django.shortcuts import render

# Create your views here.


def home(req):
    context = {'info': 'Hello there'}
    return render(req, 'base/home.html', context)
