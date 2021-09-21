from myappcabahug.models import Appointment, StaffList, User
from django.shortcuts import render
from django.views.generic import View
from myappcabahug import views
from .forms import *

# Create your views here.

class MyIndexView(View):
	def get(self, request):
		return render (request,'index.html', {})

class MySignInView(View):
	def get(self, request):
		return render (request,'signin.html', {})	
				
class MySignUpView(View):
	def get(self, request):
		return render (request,'signup.html', {})
class MyAppointmentView(View):
	def get(self, request):
		return render (request,'appointment.html', {})		
class MyStaffView(View):
	def get(self, request):
		return render (request,'staff.html', {})				

class MyTablesView(View):
	def get(self, request):
		users = User.objects.all()	
		appointments = Appointment.objects.all()	
		stafflists = StaffList.objects.all()				
		context = {
			'users': users,
			'appointments': appointments,
			'stafflists': stafflists
		}
		return render (request,'tables.html', context)	

class MyDashBoardView(View):
	def get(self, request):

		return render (request,'dashboard.html', {})
