from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello Animesh you are at the poll's index!!")
