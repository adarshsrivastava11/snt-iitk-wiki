from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from wiki.models import *
import os
from django.contrib.auth import authenticate,login
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail

def main_page(request):
	template = get_template('index.html')
	team = Team.objects.all()

	variables = Context({
		'message':'Welcome to SnT',
		'team':team,
		})
	output = template.render(variables)
	return HttpResponse(output)

def signup_page(request):
	
	team_all = Team.objects.all()
	stuname = request.POST.get('name',False)
	roll = request.POST.get('roll',False)
	roll = int(roll)
	username = request.POST.get('username',False)
	password= request.POST.get('password',False)
	teamname = request.POST.get('team',False)
	dd = teamname
	if username != False:
		if User.objects.filter(username=username).exists():
			return redirect('/')
		else:
			email_user = username+'@iitk.ac.in'
			user = User.objects.create_user(username=username,password=password,email=email_user)
			user.save()
			team = Team.objects.get(team_name=dd)
			stu = Student(user=user,team=team,student_name=stuname,student_roll=roll,student_username=username)
			stu.save()
	return render(request,'signup.html',{'allteams':team_all,'dd':dd})

def login_page(request):
	username = request.POST.get('username',False)
	password = request.POST.get('password',False)
	teamname=""
	if username != False:
		
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				stu = Student.objects.get(student_username=username)
				teamname=stu.team
				teamname = teamname.team_name
				teamname = teamname.replace(' ','')
				return redirect('/'+teamname+'/dashboard/')
	return render(request,'login.html')

def logout_page(request):
	logout(request)
	return redirect('/')
	#teamname = request.POST.get('teamname',False)

def handle_upload(f,teamname,filename):
	if not os.path.exists('wiki/uploads/'+teamname):
    		os.makedirs('wiki/uploads/'+teamname)
	with open('wiki/uploads/'+teamname+'/'+filename, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

@login_required
def dashboard(request,team_name):
	template = get_template('dashboard.html')
	filename=request.POST.get('filename',False)
		
	current_user = request.user.username
	stu = Student.objects.get(student_username=current_user)
	username = stu.student_username
	name_user = stu.student_name
	teamname = stu.team
	teamname = teamname.team_name
	team = Team.objects.get(team_name=teamname)
	teamname_original = teamname
	teamname = teamname.replace(' ','')

	if team_name != teamname:
		return redirect('/')

			
	info = team.team_briefinfo
	about = team.team_about
		

	
	


	variables = Context({
		'teamname':team_name,
		'name_user':name_user,
		'user_name':username,
		'team_name':teamname_original,
		'project_about':about,
		'project_info':info,
		'summary_data':team.team_data,
		'latest_update':team.team_update,

		
		})
	output = template.render(variables,request)
	return HttpResponse(output)

@login_required
def team_profile(request,team_name):
	
	current_user = request.user.username
	stu = Student.objects.get(student_username=current_user)
	username = stu.student_username
	name_user = stu.student_name
	teamname = stu.team
	teamname = teamname.team_name
	brief_info=''
	project_about=''
	team = Team.objects.get(team_name=teamname)
	teamname = teamname.replace(' ','')
	old = ''
	project_about = request.POST.get('about',False)
	
	brief_info = request.POST.get('intro',False)
	summary = request.POST.get('summary',False)

	update = request.POST.get('update',False)

	if brief_info != False:
		team.team_briefintro = brief_info
		team.team_about = project_about
		team.save()
		return redirect('/'+teamname+'/dashboard/')

	if summary != False:
		old = team.team_data
		team.team_data = old+' '+summary
		team.save()
		return redirect('/'+teamname+'/dashboard/')

	if update != False:
		team.team_update = update
		team.save()
		return redirect('/'+teamname+'/dashboard/')



	return render(request,'team.html',{'teamname':teamname})

@login_required
def report_upload(request,team_name):
	current_user = request.user.username
	stu = Student.objects.get(student_username=current_user)
	username = stu.student_username
	name_user = stu.student_name
	teamname = stu.team
	teamname = teamname.team_name
	team = Team.objects.get(team_name=teamname)
	teamname_original = teamname
	teamname = teamname.replace(' ','')

	if team_name != teamname:
		return redirect('/')

	filename = request.POST.get('filename',False)
	if filename != False:
		handle_upload(request.FILES['file'],teamname,filename)

	return render(request,'report.html',{'teamname':teamname})

def clubs_page(request):
	template = get_template('clubs.html')
	team = Team.objects.all()

	variables = Context({
		'message':'Welcome to SnT',
		'team':team,
		})
	output = template.render(variables)
	return HttpResponse(output)

def programming_club(request):
	template = get_template('programming_club.html')
	club = Club.objects.get(club_name="Programming Club")
	team = Team.objects.filter(club=club)
	variables = Context({
		'club_name':'Programming Club',
		'team':team,
		})
	output = template.render(variables)
	return HttpResponse(output)







