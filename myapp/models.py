from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True,null=True)
    objects = models.Manager()
    def __str__(self):
        return self.title
        

class UserInfo(models.Model):
    username=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=8)
    def __str__(self) -> str:
        return self.username
