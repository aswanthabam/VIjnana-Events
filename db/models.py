from django.db import models
from uuid import uuid4
class Level(models.Model):
    order = models.IntegerField(null=False, blank=False, unique=True, primary_key=True)
    name = models.CharField(null=False, blank=False, max_length=100, unique=True)
    question = models.TextField(null=False, blank=False, unique=True)
    answer = models.TextField(null=False, blank=False,unique=True)
    difficulty = models.IntegerField(null=False, blank=False)

class Participant(models.Model):
    participantId = models.IntegerField(null=False, blank=False, unique=True,primary_key=True)
    name = models.CharField(null=False, blank=False, max_length=100)
    current_order = models.IntegerField(null=False, blank=False)

class Submission(models.Model):
    submissionId = models.CharField(null=False, blank=False, unique=True, primary_key=True,default=uuid4, max_length=100)
    participantId = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='submission_participantId')
    level = models.IntegerField(null=False, blank=False)
    value = models.TextField(null=False, blank=False)
    time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    is_correct = models.BooleanField(null=False, blank=False)
