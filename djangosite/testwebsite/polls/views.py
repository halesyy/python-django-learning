from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

# || Modelling imports
from .models import Question, Choice

# || Index page, showing most recent polls questions
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, "polls/index.html", context)

# || Printing details about the applicable choices.
def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    c = Choice.objects.filter(question=q.id)
    context = {
        "question": q,
        "choices": c,
        "question_id": question_id
    }
    return render(request, "polls/detail.html", context)

# || Displaying the results for the 2nd bU poll
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# || Voting for 2nd bU poll
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
