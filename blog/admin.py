from django.contrib import admin
from .models import Post,Tweet,Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Tweet)
admin.site.register(Comment)