from django.views.generic.base import View
from django.shortcuts import render

from backend.models import *

class HomePage(View):
	def get(self, request):
		return render(request, 'index.html')