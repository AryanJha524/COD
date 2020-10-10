from django.urls import path

from . import views

urlpatterns = [
    path('', views.need_toilet, name='need-toilet'),
    path('create_post/', views.create_post, name='create-post'),
]
