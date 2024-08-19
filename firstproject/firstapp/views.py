from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# from django.shortcut import get_object_or_404,redirect
# from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def lastpage(request):
    template = loader.get_template('lastpage.html')
    return HttpResponse(template.render())



