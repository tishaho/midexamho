from django.db import models
from datetime import datetime

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

class Candidate(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    position = models.ForeignKey(Position,
                on_delete=models.CASCADE,
                related_name='positions',
                null=True, blank=True)
    birthdate = models.DateField("Birthdate")
    platform = models.TextField(max_length=500)

    def __str__(self):
        return 'Candidate: {}'.format(self.firstname)


class Vote(models.Model):
    candidate = models.ForeignKey(Candidate,
                on_delete=models.CASCADE,
                related_name='candidates',
                null=True, blank=True)
    vote_datetime = models.DateTimeField(default=datetime.now)
