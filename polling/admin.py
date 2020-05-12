from django.contrib import admin
from polling.models import Poll
from blogging.models import Post

admin.site.register(Poll)
admin.site.register(Post)
# Register your models here.
