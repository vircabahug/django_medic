from django.http.response import HttpResponse
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
		users = User.objects.all() # TODO: CHANGE THIS TO LOGGED IN USER
		context= {
			'users': users
		}
		return render (request,'appointment.html', context)	

	def post(self, request):		
		form = AppointmentForm(request.POST)		

		if form.is_valid():
			user = User.objects.get(user_id=request.POST.get("user_id"))

			email = request.POST.get("email")
			phone = request.POST.get("phone")
			date = request.POST.get("date")
			gender = request.POST.get("gender")
			address = request.POST.get("address")
			message = request.POST.get("message")
			app = Appointment(email = email, phone = phone, date = date, gender = gender, address = address, message = message)

			staffList = StaffList(user_id=user,appointment_id=app)
			app.save()	
			staffList.save()
		
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

	def post(self, request):
		if request.method == 'POST':	
			if 'btnUpdateUser' in request.POST:	
				print('update profile button clicked')
				userid = request.POST.get("user-userid")
				email = request.POST.get("user-email")			
				firstname = request.POST.get("user-firstname")
				lastname = request.POST.get("user-lastname")
				password = request.POST.get("user-password")
			
				# email = request.POST.get("student-email")
				# phone = request.POST.get("student-phone")
				update_user = User.objects.filter(user_id = userid).update(email = email, lastname= lastname, firstname= firstname, password = password )								  
				print(update_user)
			elif 'btnDeleteUser' in request.POST:	
				userid = request.POST.get("uuserid")
				user = User.objects.filter(user_id = userid).delete()
				
		
		return redirect('my_tables_view')

	
	
	
class MyDashBoardView(View):
	def get(self, request):

		return render (request,'dashboard.html', {})
		
