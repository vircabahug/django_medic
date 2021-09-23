from django import forms
from .models import *

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields= ('email','password')

class AppointmentForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields= ('email', 'phone')

class StaffListForm(forms.ModelForm):
	class Meta:
		model = StaffList
		fields= '__all__'                    