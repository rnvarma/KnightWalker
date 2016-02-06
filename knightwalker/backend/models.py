from __future__ import unicode_literals

from django.db import models

"""
UserData
 name(charField)
 andrewID(charField)
 gender(charField)
 schoolyear(integerField)
 home_location(coordinates)
 avg_rating(floatField)

Trip
 departure time (timeField)
 start_location (coordinates)
 dest_location (coordinates)
 description (textfield)
 creator (UserData-ForeignKey)
 attendees (UserData-ManyToMany)
 time_posted(timeField)
 completed(booleanField)

Feedback
 rater(UserData-ForeignKey)
 ratee(UserData-ForeignKey)
 num_stars(integerField)
 comment(textField)
 trip(Trip-ForeignKey)

ChatMessage
 person (UserData-ForeignKey)
 trip (Trip-ForeignKey)
 message (textField)
 time_posted (timeField)

"""

# Create your models here.

class Posts(models.Model):
	message = models.TextField(default="")
	creator = models.CharField(default="", max_length=50)
	num_likes = models.IntegerField(default=0)