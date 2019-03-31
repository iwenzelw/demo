from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='barviha-home'),
    path('blog/', views.list_1, name='barviha-list_1'),
    path('list_2/', views.list_2, name='barviha-list_2'),
    path('list_3/', views.list_3, name='barviha-list_3'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),

]
