from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

class index(request):
    return render(request, 'index.html', )
