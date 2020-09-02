from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('news/<int:pk>/', views.news_detail, name="news_detail"),

]

