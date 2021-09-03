from django.db import models

# Create your models here.
class Qualification(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Expert(models.Model):
    expertname = models.CharField(max_length=100)
    dob= models.DateField()
    doj= models.DateField()
    hospital = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    qualification= models.ForeignKey(Qualification,on_delete=models.CASCADE)

