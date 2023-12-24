# Here we're importing Django's function path and
# all of our views from the blog application.

from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name = 'post_list'),   
    path('post/<int:pk>/',views.post_detail, name = 'post_detail'),   
]

