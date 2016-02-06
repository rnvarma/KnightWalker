from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone

class UserData(models.Model):
	name = models.CharField(max_length=100, default="")
	andrewID = models.CharField(max_length=50, default="")
	gender = models.CharField(max_length=50, default="")
	schoolyear = models.IntegerField(default=2017)
	home_lat = models.FloatField(default=0)
	home_lon = models.FloatField(default=0)
	user = models.OneToOneField(settings.AUTH_USER_MODEL, default=0, related_name="userdata")
	avg_rating = models.FloatField(default=0)

class Trip(models.Model):
	departure_time = models.TimeField(null=True, blank=True)
	start_lat = models.FloatField(default=0)
	start_lon = models.FloatField(default=0)
	dest_lat = models.FloatField(default=0)
	dest_lon = models.FloatField(default=0)
	description = models.TextField(default="")
	creator = models.ForeignKey(UserData, related_name="trips")
	attendees = models.ManyToManyField(UserData, related_name="attended_trips")
	time_posted = models.DateTimeField(default=timezone.now)
	completed = models.BooleanField(default=False)

class Feedback(models.Model):
	rater = models.ForeignKey(UserData, related_name="ratings_given")
	ratee = models.ForeignKey(UserData, related_name="ratings_received")
	num_stars = models.IntegerField(default=0)
	comment = models.TextField(default="")
	trip = models.ForeignKey(Trip, related_name="feedback")

class ChatMessage(models.Model):
	poster = models.ForeignKey(UserData, related_name="comments")
	trip = models.ForeignKey(Trip, related_name="chat_messages")
	message = models.TextField(default="")
	time_posted = models.DateTimeField(default=timezone.now)

