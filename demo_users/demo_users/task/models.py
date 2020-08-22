from django.db import models
from django.contrib.auth.models import User


class task(models.Model):
    
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    date=models.DateField()
    personal=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name