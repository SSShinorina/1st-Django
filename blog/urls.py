from django.urls import path, include
from post.views import post_index

urlpatterns = [
    path('path-index/', post_index, name='post_index'),
]
