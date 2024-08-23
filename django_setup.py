from django.db import models

class Status(models.Model):
    status = models.CharField(max_length=15)

class Tasks(models.Model):
    title = models.CharField(max_lengs = 50)
    description = models.TextField()
    user = models.ForeignKey('user_and_roles.user', on_delete=models.CASCADE)