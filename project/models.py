from django.db import models

# Create your models here.
class Proj(models.Model):
    name = models.CharField(max_length=100)
    repo1 = models.CharField(max_length=100,blank=True, null=True )
    repo2 = models.CharField(max_length=100,blank=True, null=True )
    web = models.CharField(max_length=100,blank=True, null=True )
    