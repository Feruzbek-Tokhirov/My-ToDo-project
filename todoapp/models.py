from django.db import models
from django.contrib.auth import get_user_model
from .constants import TODO

# Create your models here.

User = get_user_model()


class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=TODO.STATUS.Constants, default=0)
    priority = models.IntegerField(choices=TODO.PRIORITY.Constants, default=2)
    deadline = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=202)
    content = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-priority']

    def __str__(self):
        return self.title


class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name
