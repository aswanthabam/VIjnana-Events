from django.db import models

# Create your models here.
class Task(models.Model):
	order = models.IntegerField(default=None,unique=True,blank=False,null=False)
	code = models.TextField(default=None,unique=True,blank=False,null=False)
	hint_html = models.TextField(default=None,unique=True,blank=False,null=False)
	