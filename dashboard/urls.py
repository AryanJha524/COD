from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_toilet/', views.have_toilet, name='post_toilet'),

]
