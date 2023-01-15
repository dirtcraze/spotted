from django.db import models
from django.utils import timezone

class Fitnessforlife(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user_ip = models.GenericIPAddressField()
    device = models.CharField(max_length=255)

class Fitnesstrzykorony(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user_ip = models.GenericIPAddressField()
    device = models.CharField(max_length=255)

class Halnygym(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user_ip = models.GenericIPAddressField()
    device = models.CharField(max_length=255)

class Oxygym(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user_ip = models.GenericIPAddressField()
    device = models.CharField(max_length=255)

class Xtremefitness(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user_ip = models.GenericIPAddressField()
    device = models.CharField(max_length=255)