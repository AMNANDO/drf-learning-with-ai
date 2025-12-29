from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    isActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.name
