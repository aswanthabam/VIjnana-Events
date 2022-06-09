from django.db import models

# Create your models here.
class Game(models.Model):
	team = models.OneToOneField('home.Team',default = None,blank = False,null = False,on_delete=models.CASCADE)
	one = models.DateTimeField(default = None,blank = True,null = True)
	two = models.DateTimeField(default = None,blank = True,null = True)
	three = models.DateTimeField(default = None,blank = True,null = True)
	four = models.DateTimeField(default = None,blank = True,null = True)
	five = models.DateTimeField(default = None,blank = True,null = True)
	six = models.DateTimeField(default = None,blank = True,null = True)
	seven = models.DateTimeField(default = None,blank = True,null = True)
	eight = models.DateTimeField(default = None,blank = True,null = True)
	nine = models.DateTimeField(default = None,blank = True,null = True)
	ten = models.DateTimeField(default = None,blank = True,null = True)
	eleven = models.DateTimeField(default = None,blank = True,null = True)
	twelve = models.DateTimeField(default = None,blank = True,null = True)
	twelve2 = models.DateTimeField(default = None,blank = True,null = True)
class Team(models.Model):
	team_id = models.TextField(default=None,unique=True,blank=False,null=False)
	members = models.TextField(default=None,unique=True,blank=False,null=False)
	progress = models.IntegerField(default=0,blank=False,null=False)
	
class Task(models.Model):
	order = models.IntegerField(default=None,unique=True,blank=False,null=False)
	code = models.TextField(default=None,unique=True,blank=False,null=False)
	hint_html = models.TextField(default=None,unique=True,blank=False,null=False)
	