"""
Serializers
"""
import logging

from rest_framework import serializers

import todolistapp.models as models

# Get an instance of a logger
logger = logging.getLogger('ozp-center')

class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.List
        fields = ('title', 'desc')
