from django.shortcuts import render

from django.http import HttpResponse 

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You are looking at Question %s." % question_id)

def results(resquest, question_id):
    return HttpResponse("You are looking at the results of Question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on Question %s." % question_id)