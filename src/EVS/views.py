from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import SignUpForm, FeedbackForm
from .models import SignUp, Feedback

# Create your views here.
def home(request):
	return render(request, "index.html", {})

def route(request):
	return render(request, "route.html", {})

def feedback(request):
	if request.method == "POST":
		if request.user.is_active:
			
			form = FeedbackForm(request.POST)

			if form.is_valid():
				bus_number = request.POST['bus_number']
				feedback = request.POST['feedback']
				first_name = request.user.first_name
				last_name = request.user.last_name

				#add info to our database
				Feedback(bus_number = bus_number, feedback = feedback, first_name = first_name, last_name = last_name).save()

				context = {
					'message' : 'Thank you for your feedback.'
				}
				return render(request, "success.html", context)
			else:
				form = SignUpForm()
		else:
			context = {
				'message' : 'You are not logged in. Please login to give your feedback.'
			}
			return render(request, "success.html", context)

	return render(request, "feedback.html", {})

def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
			
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		mobile_number = request.POST['mobile_number']
		password = request.POST['password']

		#check if user already exists
		if User.objects.filter(username=mobile_number).exists():
			context = {
				'message' : 'Mobile number already exists. Please register with a different mobile number.'
			}

			return render(request, "success.html", context)
		else:
			#add info to our database
			SignUp(first_name = first_name, last_name = last_name, mobile_number = mobile_number).save()

			#create user for django authentication
			user = User.objects.create_user(username = mobile_number, password = password, first_name = first_name, last_name = last_name)
			user.save()

	context = {
		'message' : 'You have been successfully registered.'
	}

	return render(request, "success.html", context)

def login_check(request):
	if request.method == "POST":
		username = request.POST['mobile_number']
		password = request.POST['password']

		user = authenticate(username = username, password = password)

		if user is not None:
			if user.is_active:				
				login(request, user)

				return render(request, "index.html", {})
		else:
			return render(request, "login-fail.html", {})

def log_out(request):
	logout(request)

	return render(request, "index.html", {})