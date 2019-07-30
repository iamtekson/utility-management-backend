from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('indexx', views.indexx, name = 'indexx'),
	path('point_dataset', views.point_dataset, name= 'point_dataset'),
	path('nepal_dataset', views.nepal_dataset, name = 'nepal_dataset'),
	path('about', views.about, name = 'about'),
	path('contact', views.contact, name = 'contact'),
	
]