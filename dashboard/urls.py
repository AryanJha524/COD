from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detailed_view/<int:pk>', views.detailed_view, name='detailed-view'),
    path('post_toilet/', views.have_toilet, name='post_toilet'),

]
