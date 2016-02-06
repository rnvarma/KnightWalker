from django.views.generic.base import View
from django.shortcuts import render

from backend.models import *

class HomePage(View):
	def get(self, request):
		posts = Posts.objects.all()
		context = {}
		context["posts"] = posts
		return render(request, 'index.html', context)