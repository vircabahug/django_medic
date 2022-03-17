from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from matplotlib.style import context
from myappcabahug import views
from.models import *
from .forms import *
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('my_index_view')

class AuthUser:

    def getUserLogged(request):
        logged_in_user = False
        if request.user.is_authenticated:
            logged_in_user = request.user
        return logged_in_user

class MyIndexView(View):
	def get(self, request):
		
		context = {
				'logged_in_user' : AuthUser.getUserLogged(request)
			}
		return render (request,'index.html',context)
        
 
		

class MySignInView(View):
	def get(self, request):
		return render (request,'signin.html', {})	

	def post(self, request):
		username = request.POST.get("username")
		pw = request.POST.get("password")
		user = authenticate(request,username=username, password=pw)
		if user is not None:
			login(request, user)
			return redirect('my_index_view')
		else:
			messages.Error(request, "User Does not exist")
			return redirect('my_signin_view')


class MySignUpView(View):
	def get(self, request):
		return render (request,'signup.html', {})

	def post(self, request):		
		form = UserForm(request.POST)	

		if form.is_valid():
			username =request.POST.get("username")
			fname = request.POST.get("firstname")
			lname = request.POST.get("lastname")
			email = request.POST.get("email")
			pw = request.POST.get("password")
			rpw = request.POST.get("re_password")
			if(User.objects.filter(email=email).exists()):
				messages.Error(request,"Email already exists")
				return redirect('my_signup_view')
			else:				
				form = User(username = username, firstname = fname, lastname = lname, email = email, password = pw, confirmpassword = rpw)
				form.save()

				DjangoUser.objects.create_user(username,email,pw)
				return redirect('my_signin_view')
		else:
			print(form.errors)
			return HttpResponse('not valid')	

		
		
class MyReservationView(View):
	def get(self, request):
		loggedUser = AuthUser.getUserLogged(request)		
		user = User.objects.get(username=loggedUser) # TODO: CHANGE THIS TO LOGGED IN USER
		context= {
			'user': user
			
			
		}
		return render (request,'appointment.html', context)	

	def post(self, request):		
		form = ReservationForm(request.POST)		

		if form.is_valid():
			user = User.objects.get(user_id=request.POST.get("user_id"))

			timeslot = request.POST.get("timeslot")
			date = request.POST.get("date")		
			roomtype = request.POST.get("roomtype")
			app = Reservation(timeslot = timeslot, date = date, roomtype = roomtype)

			#conference = Conference(user_id=user,conferenceid=app)
			app.save()	
			#conference.save()
		
			return redirect('my_index_view')
	
		else:
			print(form.errors)
			return HttpResponse('not valid')				

class MyTablesView(View):
	def get(self, request):
		users = User.objects.all()	
		reservation = Reservation.objects.all()	
		conference = Conference.objects.all()				
		context = {
			'users': users,
			'reservations': reservation,
			'conferences': conference,
		}
		return render (request,'tables.html', context)	

	def post(self, request):
		if request.method == 'POST':	
			if 'btnUpdateUser' in request.POST:	
				print('update profile button clicked')
				userid = request.POST.get("user-userid")
				username = request.POST.get("user-username")
				email = request.POST.get("user-email")			
				firstname = request.POST.get("user-firstname")
				lastname = request.POST.get("user-lastname")
				password = request.POST.get("user-password")
			
			
				update_user = User.objects.filter(user_id = userid).update(username = username, email = email, lastname= lastname, firstname= firstname, password = password )								  
				print(update_user)
			elif 'btnDeleteUser' in request.POST:	
				userid = request.POST.get("uuserid")
				user = User.objects.filter(user_id = userid).delete()
			elif 'btnUpdateReservation' in request.POST:	
				print('update profile button clicked')
				reservationid = request.POST.get("reservation-reservationid")
				timeslot = request.POST.get("reservation-timeslot")			
				date = request.POST.get("reservation-date")
				roomtype = request.POST.get("reservation-roomtype")
				
				# email = request.POST.get("student-email")
				# phone = request.POST.get("student-phone")
				update_reservation = Reservation.objects.filter(reservation_id = reservationid).update(timeslot = timeslot,  date= date,  roomtype = roomtype )								  
				print(update_reservation)
			elif 'btnDeleteReservation' in request.POST:	
				reservationid = request.POST.get("reservationid")
				reservation = Reservation.objects.filter(reservation_id = reservationid).delete()	
		
		return redirect('my_tables_view')

	
	
	

		


class MyDashBoardView(View):
	def get(self, request):

		conference_rooms = ('Conference','U-Shape','Classroom','Theater')
		date = request.GET.get('checkDate')

		maxroom = Reservation.objects.raw(
				"SELECT reservation_id,roomtype FROM myappcabahug_reservation GROUP BY roomtype ORDER BY COUNT(*) DESC LIMIT 1"
			)

		ava_rooms = []
		if(date is not None):
			available = Reservation.objects.raw("SELECT * FROM myappcabahug_reservation WHERE date='"+date+"'")

			for cr in conference_rooms:
				valid = True
				for room in available:
					type = room.roomtype
					if(type == cr):
						valid = False
				if(valid):
					ava_rooms.append(cr)
		else:
			ava_rooms = conference_rooms
		
		context = {"maxroom": maxroom,
			"a_rooms": ava_rooms
		}

		return render(request, "dashboard.html", context)



