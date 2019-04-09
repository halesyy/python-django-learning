from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Modelling imports
from .models import Question, Choice

# Show the 5 most recent polls
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, "polls/index.html", context)

def test(request):
    return HttpResponse("You just went to /test")

# The information regarding the 2nd bU
def detail(request, question_id):
    q = Question.objects.filter(pk=question_id)
    c = Choice.objects.filter(question=q.get().id)
    context = {
        "question": q.get() if q.exists() else False,
        "choices": c if c.exists() else False,
        "question_id": question_id
    }
    return render(request, "polls/detail.html", context)

    return HttpResponse("You're looking at question %s." % question_id)

# Displaying the results for the 2nd bU poll
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# Voting for 2nd bU poll
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
