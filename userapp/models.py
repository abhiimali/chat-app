from django.db import models

from django.contrib.auth.models import User


# Create your models here.\


# Message Model 

class Message(models.Model):
    
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='name')
    message  = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)




