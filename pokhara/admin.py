from django.contrib import admin
from .models import information


class informationAdmin(admin.ModelAdmin):
	list_display = ('title', 'location')
admin.site.register(information, informationAdmin)
