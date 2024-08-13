#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by rezaei.pooriya99@gmail.com on 13.08.2024

import geopandas as gpd
from typing import Tuple
from .config import GeometryType


def categorize_geometries(gdf: gpd.GeoDataFrame) -> Tuple[
    gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame]:
    """
    Categorize geometries into points, lines, polygons, and others.
    :param gdf: Combined GeoDataFrame with all features.
    :return: Tuple of GeoDataFrames categorized by geometry types.
    """
    points = gdf[gdf.geometry.geom_type.isin([GeometryType.POINT.value, GeometryType.MULTIPOINT.value])]
    lines = gdf[gdf.geometry.geom_type.isin([GeometryType.LINESTRING.value, GeometryType.MULTILINESTRING.value])]
    polygons = gdf[gdf.geometry.geom_type.isin([GeometryType.POLYGON.value, GeometryType.MULTIPOLYGON.value])]
    linear_rings = gdf[gdf.geometry.geom_type == GeometryType.LINEARRING.value]
    geometry_collections = gdf[gdf.geometry.geom_type == GeometryType.GEOMETRYCOLLECTION.value]

    return points, lines, polygons, linear_rings, geometry_collections
