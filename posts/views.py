from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from django.urls import reverse
from django.views import generic
from django.utils import timezone

from django.utils.datastructures import MultiValueDictKeyError

from .models import Post
from . import functions

import datetime

class StartView(generic.ListView):
    template_name = 'posts/start.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """
        Return all posts, sorted by date
        """
        return Post.objects.order_by('-pub_date')


def create_post(request):

    if request.POST:

        try:
            post = request.POST['post_text']
        except MultiValueDictKeyError:
            post = ""

        if post == "":
            return render(request, 'posts/create_new_post.html')
        else:
            # --- publish the post ---
            # get current date
            date = datetime.datetime.now()
            # get current user id
            user_id = request.user.id
            # is it private?
            private = not request.POST['public_post']

            functions.add_new_post(post, date, user_id, private, False)
            strin = "'" + post + "'"
            return HttpResponse(strin)
    else:
        return render(request, 'posts/create_new_post.html')

