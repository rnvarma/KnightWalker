from django.views.generic.base import View
from django.shortcuts import render

from backend.models import *

class HomePage(View):
	def get(self, request):
		user = request.user
		if not UserData.objects.filter(user=user).count():
			email = user.email
			andrewID = email.split("@")[0]
			name = user.first_name + " " + user.last_name
			ud = UserData(user=user, andrewID=andrewID, name=name)
			ud.save()
		return render(request, 'home.html')

class Login(View):
	def get(self, request):
		return render(request, 'login.html')