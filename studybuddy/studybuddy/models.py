
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
class mentor(models.Model):
    name=models.CharField(max_length=100)
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
