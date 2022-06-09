from django.db import models

# Create your models here.
class Team(models.Model):
	team_id = models.TextField(default=None,unique=True,blank=False,null=False)
	members = models.TextField(default=None,unique=True,blank=False,null=False)
	progress = models.IntegerField(default=None,blank=False,null=False)
	
class Task(models.Model):
	order = models.IntegerField(default=None,unique=True,blank=False,null=False)
	code = models.TextField(default=None,unique=True,blank=False,null=False)
	hint_html = models.TextField(default=None,unique=True,blank=False,null=False)
	