from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Token(models.Model):
    token=models.CharField(max_length=50)
    nam=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.nam)
    
class Dakhl(models.Model):
    tozih=models.CharField(max_length=100)
    tarikh=models.DateTimeField()
    mablagh=models.BigIntegerField()
    nam=models.ForeignKey(User)
    def __str__(self):
        return "{}".format(self.mablagh)
class Kharj(models.Model):
    tozih=models.CharField(max_length=100)
    tarikh=models.DateTimeField()
    mablagh=models.BigIntegerField()
    nam=models.ForeignKey(User)
    def __str__(self):
        return "{}".format(self.mablagh)