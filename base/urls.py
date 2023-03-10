from django.urls import path
from . import views

urlpatterns = [
      path('', views.index, name = "index"),
      path('trends/', views.get_trends, name= "trends"),
      path('tweets/', views.get_tweets, name= "tweets"),
      
]