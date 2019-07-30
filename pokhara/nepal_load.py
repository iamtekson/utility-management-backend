import os
from django.contrib.gis.utils import LayerMapping
from .models import nepal

# Auto-generated `LayerMapping` dictionary for nepal model
nepal_mapping = {
    'objectid': 'OBJECTID',
    'district': 'DISTRICT',
    'gapa_napa': 'GaPa_NaPa',
    'type_gn': 'Type_GN',
    'zone': 'ZONE',
    'region': 'REGION',
    'state_code': 'STATE_CODE',
    'geom': 'MULTIPOLYGON',
}

nepal_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../static/data/admin_nepal/ADMIN_NEPAL.shp'),
)



def run(verbose=True):
    lm = LayerMapping(nepal, nepal_shp, nepal_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)