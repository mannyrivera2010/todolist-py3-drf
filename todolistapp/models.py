import uuid
from django.db import models

class List(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=50)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title


class Item(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title
        
