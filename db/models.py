from django.db import models

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
    participantId = models.ForeignKey(Participant, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    value = models.TextField(null=False, blank=False)
    time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    is_correct = models.BooleanField(null=False, blank=False)
