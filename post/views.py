from django.http import HttpResponse
from django.shortcuts import render


def post_index(request):
    return HttpResponse("Hello, Jibon.")