"""
Models for use with the Admin interface

Available at /admin

run python manage.py createsuperuser to create an admin user/password
"""

from django.contrib import admin

import todolistapp.models as models

# Register models for admin interface

admin.site.register(models.List)
admin.site.register(models.Item)
