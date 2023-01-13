from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('fitnessforlife/', views.fitnesstrzykorony, name='Fitness for Life - Nowy Sącz'),
    path('fitnesstrzykorony/', views.fitnessforlife, name='Fitness Trzy Korony'),
    path('halnygym/', views.halnygym, name='HALNY Nowy Sącz'),
    path('oxygym/', views.oxygym, name='Oxy Gym Nowy Sącz'),
    path('xtremefitness/', views.xtremefitness, name='Xtreme Fitness Nowy Sącz'),
    path('submit/', views.submit_view, name='submit_url'),
]