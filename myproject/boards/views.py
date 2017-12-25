import django.contrib.auth.models
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.urls import reverse

from .forms import NewTopicForm, PostForm
from .models import Board, Post, Topic

def home(request):
    boards = Board.objects.all ()
    return render (request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404 (Board, pk=pk)
    return render (request, 'topics.html', {'board': board})


def new_topic(request, pk):
    board = get_object_or_404 (Board, pk=pk)
    user = django.contrib.auth.models.User.objects.first ()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm (request.POST)
    if form.is_valid ():
        topic = form.save ()
        return redirect ('board_topics', pk=board.pk)

    else:
        form = NewTopicForm ()
        return render (request, 'new_topic.html', {'form': form})
