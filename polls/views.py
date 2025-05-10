from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.http import HttpRequest, HttpResponse
# Create your views here.
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse



# Vista de lista genérica
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

def owner(request):
    return HttpResponse("Hello, world. 071b5ec6 is the index of the polls.")


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

# Vista de detalle genérica
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

# Vista de resultados genérica
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "No seleccionaste una opción.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))