from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('news/', views.NewsView.as_view(), name="news"),
    path('menu/', views.MenuView.as_view(), name="menu"),
    path('contact/', views.ContactView.as_view(), name="contact"),
]