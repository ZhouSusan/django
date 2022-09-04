from django.shortcuts import render

from django.http import HttpResponse 

def index(request):
    last_question_list = Question.objects.order_by('pub_date')[:5]
    output = ','.join([q.question_text for q in last_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You are looking at Question %s." % question_id)

def results(resquest, question_id):
    return HttpResponse("You are looking at the results of Question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on Question %s." % question_id)