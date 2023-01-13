from django.db import models

class Fitnessforlife(models.Model):
  message = models.CharField(max_length=255)
  currTime = models.TimeField()
  currDate = models.DateField()

class Fitnesstrzykorony(models.Model):
  message = models.CharField(max_length=255)
  currTime = models.TimeField()
  currDate = models.DateField()

class Halnygym(models.Model):
  message = models.CharField(max_length=255)
  currTime = models.TimeField()
  currDate = models.DateField()

class Oxygym(models.Model):
  message = models.CharField(max_length=255)
  currTime = models.TimeField()
  currDate = models.DateField()

class Xtremefitness(models.Model):
  message = models.CharField(max_length=255)
  currTime = models.TimeField()
  currDate = models.DateField()