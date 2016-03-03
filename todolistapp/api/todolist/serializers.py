"""
Serializers
"""
import logging

from rest_framework import serializers
import todolistapp.models as models

'''
from rest_framework.renderers import JSONRenderer
import todolistapp.models as models;import todolistapp.serializers as serializers
JSONRenderer().render(serializers.ListSerializer(models.List.objects.all()[0]).data)
'''

# Get an instance of a logger
logger = logging.getLogger('todoapplist')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoItem
        fields = ('id','title')
        read_only_fields = ('id',)

class ListSerializer(serializers.ModelSerializer):
    todoitem_set = ItemSerializer(many=True)

    class Meta:
        model = models.TodoList
        fields = ('id', 'title', 'todo_set')
        read_only_fields = ('id',)
