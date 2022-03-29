from django.db import models

# Create your models here.
class students(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    stu_id = models.IntegerField()

def __str__(self):
    return self.fname
