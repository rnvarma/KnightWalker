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

class TripPage(View):
	def get(self,request):
		return render(request, 'trip.html')
		
class WhereToGoPage(View):
	def get(self, request):
		return render(request, 'where_to_go_3.0.html')

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

class RecommendList(View):
	def get(self, request):
		trips = Trip.objects.all()
		trips_data = []
		for trip in trips:
			data = {}
			data["creator"] = trip.creator
			data["start_lon"] = trip.start_lon
			data["start_lat"] = trip.start_lat
			data["dest_lat"] = trip.dest_lat
			data["dest_lon"] = trip.dest_lon
			data["description"] = trip.description
			data["start_time"] = trip.departure_time
			data["id"] = trip.id
			# data["attendees"] = trip.attendees
			trips_data.append(data)
		context = {}
		context["trip_list"] = trips_data
		return render(request, 'recommendList.html', context)

class Chat(View):
	def get(self, request):
		return render(request, 'chat.html')





