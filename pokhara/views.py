from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import nepal,information

def index(request):
	return render(request, 'pages/index.html')

def indexx(request):
	return render(request, 'indexx.html')

def nepal_dataset(request):
	Nepal = serialize('geojson', nepal.objects.all())
	return HttpResponse(Nepal, content_type = 'json')

def point_dataset(request):
	points = serialize('geojson', information.objects.all())
	return HttpResponse(points,content_type='json')

def about(request):
	return render(request, 'pages/about.html')

def contact(request):
	return render(request, 'contact/contact.html')
