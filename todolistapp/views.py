"""
Views
"""
import logging

from rest_framework import viewsets

import todolistapp.models as models
import todolistapp.serializers as serializers

# Get an instance of a logger
logger = logging.getLogger('todolistapp')

class ListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.List.objects.all()
    serializer_class = serializers.ListSerializer
