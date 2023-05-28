from django.db import models

class ElderlyPerson(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class Medication(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    schedule_time = models.TimeField()
    elderly_person = models.ForeignKey(ElderlyPerson, on_delete=models.CASCADE)
