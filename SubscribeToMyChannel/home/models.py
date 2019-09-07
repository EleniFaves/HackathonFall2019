# Create your models here.
from __future__ import unicode_literals
from django.db import models
class Counter(models.Model):
 count = models.IntegerField(blank=False, default=0)