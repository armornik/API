from django.db import models


# Create your models here.
class SearchUser(models.Model):
    username = models.CharField(max_length=256, unique=True)
