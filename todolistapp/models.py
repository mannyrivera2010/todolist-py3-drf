"""
File used to store all the Models for todolistapp
"""
import logging
import uuid

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Get an instance of a logger
logger = logging.getLogger('todoapplist')

class Profile(models.Model):
    """
    A User (User's Profile) on APP

    Note that some information (username, email, last_login, date_joined) is
    held in the associated Django User model. In addition, the user's role
    (USER, ADMIN) is represented by the Group
    associated with the Django User model

    Notes on use of contrib.auth.models.User model:
        * first_name and last_name are not used
        * is_superuser is always set to False
        * is_staff is set to True for Org Stewards and Apps Mall Stewards
        * password is used
    """
    display_name = models.CharField(max_length=255)
    access_control = models.CharField(max_length=16384)

    # instead of overriding the builtin Django User model used
    # for authentication, we extend it
    # https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#extending-the-existing-user-model
    user = models.OneToOneField(User, null=True, blank=True)

    def __repr__(self):
        return 'Profile: %s' % self.user.username

    def __str__(self):
        return self.user.username

class AccessControlTodoListManager(models.Manager):
    """
    Use a custom manager to control access to Listings

    Instead of using models.Listing.objects.all() or .filter(...) etc, use:
    models.Listing.objects.for_user(user).all() or .filter(...) etc

    This way there is a single place to implement this 'tailored view' logic
    for listing queries
    """
    def for_user(self, username):
        # get all TodoLists
        objects = super(AccessControlListingManager, self).get_queryset()
        return objects

class TodoList(models.Model):
    """
    Model used to store all the list of the app
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=50)
    #objects = AccessControlTodoListManager

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

class TodoItem(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title
