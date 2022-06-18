from django.urls import path

from profesor import views


app_name='profesor'
urlpatterns = [
    path('profesors', views.profesor_list, name='profesor-list'),
    path('profesor/add', views.ProfesorCreateView.as_view(), name='profesor-add'),
    path('profesor/<int:pk>/update', views.ProfesorUpdateView.as_view(), name='profesor-update'),
    path('profesor/<int:pk>/delete', views.delete_profesor, name='profesor-delete'),
]
