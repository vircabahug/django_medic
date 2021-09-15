from myappcabahug.models import Appointment, StaffList, User
from django.shortcuts import render
from django.views.generic import View
from myappcabahug import views

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

class MyDashBoardView(View):
	def get(self, request):
		users = User.objects.all()	
		appointments = Appointment.objects.all()	
		stafflists = StaffList.objects.all()				
		context = {
			'users': users,
			'appointments': appointments,
			'stafflists': stafflists
		}
		return render (request,'dashboard.html', context)

