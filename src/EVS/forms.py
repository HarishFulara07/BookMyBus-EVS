from django import forms
from .models import SignUp
from .models import Feedback

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['first_name','last_name','mobile_number']

	first_name = forms.CharField(required = True)
	last_name = forms.CharField(required = True)
	mobile_number = forms.CharField(required = True)
	password = forms.CharField(required = True)

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ['bus_number','feedback']

	bus_number = forms.CharField(required = True)
	feedback = forms.CharField(widget = forms.Textarea, required = True)