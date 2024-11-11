from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    skills = models.TextField()
    total_hours = models.FloatField(default=0)

class Shift(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    required_training = models.CharField(max_length=100, blank=True)
    max_volunteers = models.IntegerField()
    volunteers = models.ManyToManyField(Volunteer, blank=True)

class MilestoneBadge(models.Model):
    name = models.CharField(max_length=50)
    hours_required = models.IntegerField()
    description = models.TextField()
