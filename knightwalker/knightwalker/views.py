from django.views.generic.base import View
from django.shortcuts import render

from backend.models import *

class HomePage(View):
	def get(self, request):
		return render(request, 'index.html')

class WhereToGoPage(View):
	def get(self, request):
		return render(request, 'where_to_go_1.0.html')