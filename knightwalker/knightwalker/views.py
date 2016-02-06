from django.http import HttpResponseRedirect
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

class WhereToGoPage(View):
	def get(self, request):
		return render(request, 'where_to_go_1.0.html')

	def post(self, request):
		trip = Trip(
			creator = request.user.userdata,
			departure_time = request.POST.get("departure_time"),
			start_lat = request.POST.get("start_lat"),
			start_lon = request.POST.get("start_lon"),
			dest_lat = request.POST.get("dest_lat"),
			dest_lon = request.POST.get("dest_lon"),
			description = request.POST.get("description")
		)
		trip.save()
		return HttpResponseRedirect("/trip/%d" % trip.id)

class Login(View):
	def get(self, request):
		return render(request, 'login.html')
