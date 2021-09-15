from django import forms
from .models import *

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields= '__all__'

class AppointmentForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields= '__all__'

class StaffListForm(forms.ModelForm):
	class Meta:
		model = StaffList
		fields= '__all__'                    