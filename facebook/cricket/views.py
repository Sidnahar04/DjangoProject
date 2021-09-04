from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'sample.html')
    # return HttpResponse("web creyed by sid")

# Create your views here.
