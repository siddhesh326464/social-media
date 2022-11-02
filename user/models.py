from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=100)
    followers=models.IntegerField(default=0)
    following=models.IntegerField(default=0)
    image=models.ImageField()

    def __str__(self) -> str:
        return str(self.user)