from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce


# Create your models here.


class PostManager(models.Manager):
    def user_available_post(self):
        return self.filter(created=True)


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    created = models.BooleanField(default=False)

    def __str__(self):
        return self.user
