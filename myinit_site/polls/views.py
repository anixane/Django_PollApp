from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404

# '-'represents decending order
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context -> used to pass parameters to some scoped file or function loaded with loader
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {
        'question': question,
    }
    return render(request,'polls/detail.html',context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)