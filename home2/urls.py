from django.urls import path
#from django.conf.urls import url
from home2 import views

app_name='home2'
urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about_us, name='about_us'),
    #url(r'^^$', views.error_404),
    #path('search', views.search, name='search'),
]

handler404 = "home2.views.error_404"  