from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Tweet, Comment

from django.contrib import messages
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.views.decorators.csrf import csrf_exempt

import logging
import json


# Create your views here.

# home() - take request argument
# return what the user wants to see
# views always return a httpresponse or an exception
#
# # function based view
def home(request):
    context = {
        # 'posts': posts
        'tweets': Tweet.objects.all().order_by('-date_posted'),
        'comments': Comment.objects.all().order_by('-c_date_posted')
    }
    print(context)
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)


#crates the comment object
def create_comment(request):
    context = {
        # 'posts': posts
        'tweets': Tweet.objects.all().order_by('-date_posted'),
        'comments': Comment.objects.all().order_by('-c_date_posted')
    }
    if request.method == "POST":

        print("#############################################")
        data = request.POST
        file = request.FILES
        c_audio_file = file.get('c_audio_file')

        print("c_audio_file: ",c_audio_file)
        print("file: " ,file.get('c_audio_file'))
        tweet = data.get("tweet")
        print(tweet,type(tweet))
        c_author = request.user
        tweet = Tweet.objects.get(id=tweet)
        print(tweet,type(tweet))
        comment = Comment(c_audio_file=c_audio_file,c_author=c_author,tweet=tweet)
        comment.save()


        return render(request, 'blog/home.html', context)
    return render(request, 'blog/home.html',context)



class TweetCreateView(LoginRequiredMixin,
                      CreateView):  # LoginRequiredMixin- instead of login_required decorator in functional view
    model = Tweet
    fields = ['title', 'audio_file']

    # expects blog/tweet_form.html

    # we are getting error NOT NULL constraint failed: blog_post.author_id
    # so need to mention the author id
    def form_valid(self, form):
        logging.getLogger(__name__).info("check form validation")
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'about'})

