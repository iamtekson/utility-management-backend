from django.contrib import admin
from .models import information, nepal
from leaflet.admin import LeafletGeoAdmin


class informationAdmin(LeafletGeoAdmin):
	list_display = ('title', 'location')

admin.site.register(information, informationAdmin)


class adminNepalAdmin(LeafletGeoAdmin):
	list_display = ('objectid', 'gapa_napa', 'district')

admin.site.register(nepal, adminNepalAdmin)