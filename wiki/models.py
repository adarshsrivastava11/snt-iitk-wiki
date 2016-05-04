from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Club(models.Model):
	club_name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.club_name

class Team(models.Model):
	club = models.OneToOneField(Club)
	team_name = models.CharField(max_length=200)
	team_data = models.CharField(max_length=10000,default=" ")
	team_about = models.CharField(max_length=200,default="")
	team_briefinfo = models.CharField(max_length=1000,default="")
	team_update = models.CharField(max_length=100,default="")
	def __str__(self):
		return self.team_name

class Student(models.Model):
	team = models.ForeignKey(Team,on_delete=models.CASCADE)
	student_name = models.CharField(max_length=200)
	student_roll = models.IntegerField(default=0)
	student_username = models.CharField(max_length=50,default=" ")
	user = models.OneToOneField(User)
	def __str__(self):
		return self.student_username

class Updates(models.Model):
	team = models.ForeignKey(Team,on_delete=models.CASCADE)
	update = models.CharField(max_length=100)
	team_name = models.CharField(max_length=200)
	def __str__(self):
		return self.team_name




