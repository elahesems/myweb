from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('news/<str:word>/', views.news_detail, name="news_detail"),
    path('panel/news/list', views.news_list, name="news_list"),

]

