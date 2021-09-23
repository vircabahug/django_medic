from django.http.response import HttpResponse
from myappcabahug.models import Appointment, StaffList, User
from django.shortcuts import redirect, render
from django.views.generic import View
from myappcabahug import views
from.models import *
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

	def post(self, request):		
		form = UserForm(request.POST)
		
				

		if form.is_valid():

			fname = request.POST.get("firstname")
			lname = request.POST.get("lastname")
			email = request.POST.get("email")
			pw = request.POST.get("password")
			rpw = request.POST.get("re_password")
			form = User(firstname = fname, lastname = lname, email = email, password = pw, confirmpassword = rpw)
			form.save()	
		
			return redirect('my_tables_view')
	
		else:
			print(form.errors)
			return HttpResponse('not valid')	


		
class MyAppointmentView(View):
	def get(self, request):
		return render (request,'appointment.html', {})	

	def post(self, request):		
		form = AppointmentForm(request.POST)		

		if form.is_valid():

			email = request.POST.get("email")
			phone = request.POST.get("phone")
			date = request.POST.get("date")
			gender = request.POST.get("gender")
			address = request.POST.get("address")
			message = request.POST.get("message")
			form = Appointment(email = email, phone = phone, date = date, gender = gender, address = address, message = message)
			form.save()	
		
			return redirect('my_tables_view')
	
		else:
			print(form.errors)
			return HttpResponse('not valid')

		
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
