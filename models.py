from django.db import models

# Create your models here.


class phonebook(models.Model):
    Name=models.CharField(max_length=20)
    Phone=models.IntegerField()

def __str__(self):
    return  f" {self.Name}"