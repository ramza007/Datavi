import os
from django.contrib.gis.utils import LayerMapping 
from .models import counties, WordBorder


counties_mapping = {
    'objectid': 'OBJECTID',
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'county3_field': 'COUNTY3_',
    'county3_id': 'COUNTY3_ID',
    'county': 'COUNTY',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'Data/counties', 'County.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        counties, world_shp, counties_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)

wordborder_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'geom': 'MULTIPOLYGON',
}

world_shp2 = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'Data/world_borders', 'TM_WORLD_BORDERS-0.3.shp'),
)

def run_border(verbose=True):
    lm = LayerMapping(
        WordBorder, world_shp2, wordborder_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)