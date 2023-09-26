from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from polls.models import Question


# Create your views here.
def index(request):
  latest_question_list = Question.objects.order_by("-pub_date")[:15]
  output = ",".join(q.question_text for q in latest_question_list)
  return render(
    request,
    "polls/index.html",
    {
      "latest_question_list" : latest_question_list,
    },
  )

def detail(request : HttpRequest,question_id: int):
  return HttpResponse("You 're looking at question %s." % question_id)

def results(request : HttpRequest, question_id: int):
  response = "You 're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request : HttpRequest, question_id: int):
  return HttpResponse("You 're voting on question %s." % question_id)
  
  

 
 
