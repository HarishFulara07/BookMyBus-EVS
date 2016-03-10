from django.contrib import admin

# Register your models here.
from .forms import SignUpForm, FeedbackForm
from .models import SignUp, Feedback

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["first_name","last_name","mobile_number","timestamp","updated"]
	form = SignUpForm

admin.site.register(SignUp, SignUpAdmin)

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ["bus_number","feedback","first_name","last_name","timestamp","updated"]
	form = FeedbackForm

admin.site.register(Feedback, FeedbackAdmin)