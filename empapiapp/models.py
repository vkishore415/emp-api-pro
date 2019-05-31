from django.db import models

# Create your models here.
class Emp(models.Model):
    ename=models.CharField(max_length=50)
    esal=models.IntegerField()
    email=models.EmailField(max_length=100)
    def __init__(self):
        return self.ename