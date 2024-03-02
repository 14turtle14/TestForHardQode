from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    video_link = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    min_users = models.PositiveIntegerField()
    max_users = models.PositiveIntegerField()

class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
