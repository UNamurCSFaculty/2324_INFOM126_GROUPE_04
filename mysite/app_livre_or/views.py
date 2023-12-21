from django.shortcuts import render
from django.http import HttpResponse

def demo_view(request):
	return HttpResponse("This is a demo view!")



# Create your views here.
