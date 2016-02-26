"""
Urls
"""
from django.conf.urls import url, include

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'', include('todolistapp.api.todolist.urls')),
]
