from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    records = models.ManyToManyField(User, through='Record')


class Record(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    taken_at = models.DateTimeField()
