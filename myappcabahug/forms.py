from django import forms
from .models import *

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields= ('email','password')

class ReservationForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields= ('roomtype','timeslot')

class ConferenceForm(forms.ModelForm):
	class Meta:
		model = Conference
		fields= '__all__'                    