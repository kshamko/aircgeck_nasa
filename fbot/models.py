from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=200)
    fb_id = models.CharField(max_length=200)
    registration_date = models.DateTimeField(auto_now_add=True)
    current_location = models.CharField(max_length=200)
    current_lon = models.FloatField()
    current_lat = models.FloatField()
    