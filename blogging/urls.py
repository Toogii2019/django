from django.urls import path
from blogging.views import list_view, detail_view

urlpatterns = [
    path('', list_view, name="post_list"),
    path('polls/<int:post_id>/', detail_view, name="post_detail"),
]
