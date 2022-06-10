from django.urls import path

from home2 import views

app_name='home2'
urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about_us, name='about_us'),
    #path('search', views.search, name='search'),
]