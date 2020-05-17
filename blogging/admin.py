from django.contrib import admin
from polling.models import Poll
from blogging.models import Category, Post

admin.site.register(Poll)
admin.site.register(Post)
admin.site.register(Category)
