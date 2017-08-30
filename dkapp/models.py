from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Token(models.Model):
    token=models.CharField(max_length=50)
    nam=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.nam)