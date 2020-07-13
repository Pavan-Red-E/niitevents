from django import forms
from .models import join,contact,house

class joinForm(forms.ModelForm):
	class Meta:
		model = join
		fields = ('first_name','event_name','email','enrollment_no','phone_number')

class contactForm(forms.ModelForm):
	class Meta:
		model = contact
		fields = ('first_name','write_your_message_here','email','phone_number')

class houseForm(forms.ModelForm):
	class Meta:
		model = house
		fields = ('first_name','event_name','email','enrollment_no','phone_number')