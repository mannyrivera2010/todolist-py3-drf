from django.db import models

class List(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=50)

class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
