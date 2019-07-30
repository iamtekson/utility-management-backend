from __future__ import unicode_literals
from django.db import models   
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models as gis_models
from datetime import datetime

class information(models.Model):
    title = models.CharField(max_length=30)
    location = gis_models.PointField(srid = 4326)
    objects = GeoManager()
    
    def __str__(self):
        return self.title


class nepal(models.Model):
    objectid = models.FloatField()
    district = models.CharField(max_length=50)
    gapa_napa = models.CharField(max_length=50)
    type_gn = models.CharField(max_length=50)
    zone = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    state_code = models.IntegerField()
    geom = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.gapa_napa





