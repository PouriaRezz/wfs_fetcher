#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by rezaei.pooriya99@gmail.com on 13.08.2024

from enum import Enum


class GeometryType(Enum):
    POINT = "Point"
    MULTIPOINT = "MultiPoint"
    LINESTRING = "LineString"
    MULTILINESTRING = "MultiLineString"
    POLYGON = "Polygon"
    MULTIPOLYGON = "MultiPolygon"
    LINEARRING = "LinearRing"
    GEOMETRYCOLLECTION = "GeometryCollection"


FORMAT_TO_DRIVER = {
    "GeoJSON": "GeoJSON",
    "GeoPackage": "GPKG",
    "Shapefile": "ESRI Shapefile"
}
