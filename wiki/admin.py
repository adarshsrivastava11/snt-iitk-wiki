from django.contrib import admin

from .models import *
from .models import Team

class TeamInline(admin.StackedInline):
	model=Team
	extra=10

class StudentInline(admin.StackedInline):
	model = Student
	extra = 5

class TeamAdmin(admin.ModelAdmin):
	
	inlines = [StudentInline] 

class ClubAdmin(admin.ModelAdmin):
	inlines = [TeamInline]

admin.site.register(Club,ClubAdmin)
admin.site.register(Team,TeamAdmin)
#admin.site.register(Student)


