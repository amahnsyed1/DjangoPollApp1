import logging

from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from .models import Choice, Question, Profile, Answered
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
<<<<<<< Updated upstream
    question = get_object_or_404(Question, pk=question_id)
=======
    logger = logging.getLogger(__name__)

    user = request.user
    question = get_object_or_404(Question, pk=question_id)

    f1 = Answered.objects.filter(user=user, question=question)

    if f1.count() > 0:
        messages.add_message(request, messages.WARNING, 'You have already voted in this poll!')
        logger.error('Something went wrong!')
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    a = Answered(user=user, question=question)
    a.save()

>>>>>>> Stashed changes
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You did not select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
