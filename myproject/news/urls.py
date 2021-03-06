from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('news/<str:word>/', views.news_detail, name="news_detail"),
    path('panel/news/list/', views.news_list, name="news_list"),
    path('panel/news/list/', views.news_list, name="news_list"),
    path('panel/news/add/', views.news_add, name="news_add"),
    path('panel/news/del/<str:pk>/', views.news_delete, name="news_delete"),
    path('panel/news/edit/<str:pk>/', views.news_edit, name="news_edit"),

]

