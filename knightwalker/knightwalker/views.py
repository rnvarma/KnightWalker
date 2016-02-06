from django.views.generic.base import View
from django.shortcuts import render

from backend.models import *

class HomePage(View):
	def get(self, request):
<<<<<<< HEAD
		return render(request, 'index.html')
		user = request.user
=======
				user = request.user
>>>>>>> 235121b54d6ab400559a2583142bf44b8b927aa3
		if not UserData.objects.filter(user=user).count():
			email = user.email
			andrewID = email.split("@")[0]
			name = user.first_name + " " + user.last_name
			ud = UserData(user=user, andrewID=andrewID, name=name)
			ud.save()
		return render(request, 'home.html')

<<<<<<< HEAD
class Trip(View):
	def get(self,request):
		return render(request, 'trip.html')
		
=======
class WhereToGoPage(View):
	def get(self, request):
		return render(request, 'where_to_go_1.0.html')

>>>>>>> 235121b54d6ab400559a2583142bf44b8b927aa3
class Login(View):
	def get(self, request):
		return render(request, 'login.html')
