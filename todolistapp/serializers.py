"""
Serializers
"""
import logging

from rest_framework import serializers

import todolistapp.models as models

# Get an instance of a logger
logger = logging.getLogger('ozp-center')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ('id','title',)

class ListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = models.List
        fields = ('id', 'title', 'desc', 'items')
