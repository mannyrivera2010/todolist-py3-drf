"""
Views
"""
import logging

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

import todolistapp.models as models
import todolistapp.api.todolist.serializers as serializers

# Get an instance of a logger
logger = logging.getLogger('todolistapp')

class ListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.TodoList.objects.all()
    serializer_class = serializers.ListSerializer

    """
    List all
    """
    def list(self, request):
        queryset = models.TodoList.objects.all()
        serializer = serializers.ListSerializer(queryset, many=True)
        return Response(serializer.data)

        # if serializer.is_valid():
        #
        # else:
        #     return Response(serializer.errors,
        #                     status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        queryset = models.TodoList.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = serializers.ListSerializer(user)
        return Response(serializer.data)

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.TodoItem.objects.all()
    serializer_class = serializers.ItemSerializer
