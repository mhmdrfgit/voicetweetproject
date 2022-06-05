from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

import pandas as pd
from django.conf import settings
import os
from pathlib import Path


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)  # auto_now_add=True adds date when objects created
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # delete when the user gets deleted

    def __str__(self):
        return self.title

    # getting error:No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
    # when trying to post new content
    # so adding this function

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Tweet(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to="audio_files")
    date_posted = models.DateTimeField(default=timezone.now)  # auto_now_add=True adds date when objects created
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # delete when the user gets deleted

    def __str__(self):
        return self.title

    # getting error:No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
    # when trying to post new content
    # so adding this function

    def get_absolute_url(self):
        return reverse('blog-home')


class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    c_audio_file = models.FileField(upload_to="audio_files")
    c_date_posted = models.DateTimeField(default=timezone.now)  # auto_now_add=True adds date when objects created
    c_author = models.ForeignKey(User, on_delete=models.CASCADE)  # delete when the user gets deleted

    def get_absolute_url(self):
        return reverse('blog-home')
