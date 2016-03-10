from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SignUp(models.Model):
	first_name = models.CharField(max_length = 120, blank = False)
	last_name = models.CharField(max_length = 120, blank = False)	
	#maximum 120 characters allowed in full_name
	#blank = False means that form field field is mandatory
	mobile_number = models.CharField(max_length = 10, blank = False, unique = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	#auto_now_add = True and auto_now = False means timestamp will be added only once when the
	#model is created
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	#auto_now_add = False and auto_now = True means timestamp will be added everytime the model
	#is updated

class Feedback(models.Model):
	bus_number = models.CharField(max_length = 10, blank = False)
	feedback = models.CharField(max_length = 1024, blank = False)
	first_name = models.CharField(max_length = 120, blank = False, null = True)
	last_name = models.CharField(max_length = 120, blank = False, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	#auto_now_add = True and auto_now = False means timestamp will be added only once when the
	#model is created
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	#auto_now_add = False and auto_now = True means timestamp will be added everytime the model
	#is update