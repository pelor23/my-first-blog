from django.contrib import admin
from .models import Post, Comment, AboutMe


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(AboutMe)