from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('', views.main, name='about'),
    path('', views.main, name='contact'),
    path('fitnessforlife/', views.handle_form, name='fitnessforlife'),
    path('fitnesstrzykorony/', views.handle_form, name='fitnesstrzykorony'),
    path('halnygym/', views.handle_form, name='halnygym'),
    path('oxygym/', views.handle_form, name='oxygym'),
    path('xtremefitness/', views.handle_form, name='xtremefitness'),
]