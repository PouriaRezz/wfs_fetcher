#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by rezaei.pooriya99@gmail.com on 13.08.2024

import os
import geopandas as gpd
from typing import List
import logging
from .config import FORMAT_TO_DRIVER


def save_geodataframes(
        points: gpd.GeoDataFrame,
        lines: gpd.GeoDataFrame,
        polygons: gpd.GeoDataFrame,
        linear_rings: gpd.GeoDataFrame,
        geometry_collections: gpd.GeoDataFrame,
        output_dir: str,
        format: str
) -> None:
    """
    Save GeoDataFrames based on geometry types in the specified format.
    :param points: GeoDataFrame containing point and multipoint geometries.
    :param lines: GeoDataFrame containing line and multiline geometries.
    :param polygons: GeoDataFrame containing polygon and multipolygon geometries.
    :param linear_rings: GeoDataFrame containing linear ring geometries.
    :param geometry_collections: GeoDataFrame containing geometry collection geometries.
    :param output_dir: Directory where output files will be saved.
    :param format: File format to save the GeoDataFrames (GeoJSON, GeoPackage, or Shapefile).
    """
    driver = FORMAT_TO_DRIVER.get(format)

    if driver is None:
        logging.error(f"Unsupported format: {format}")
        raise ValueError(f"Unsupported format: {format}")

    def save_gdf(gdf: gpd.GeoDataFrame, filename: str) -> None:
        """Helper function to save a GeoDataFrame in the specified format."""
        gdf.to_file(os.path.join(output_dir, filename), driver=driver)
        logging.info(f"Saved {filename} as {format}")

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    format_extension = {
        "GeoJSON": "geojson",
        "GeoPackage": "gpkg",
        "Shapefile": "shp"
    }.get(format, "geojson")

    # Define filenames based on geometry types
    filenames = {
        'points': "points_and_multipoints." + format_extension,
        'lines': "lines_and_multilines." + format_extension,
        'polygons': "polygons_and_multipolygons." + format_extension,
        'linear_rings': "linear_rings." + format_extension,
        'geometry_collections': "geometry_collections." + format_extension
    }

    # Save GeoDataFrames for each geometry type
    if not points.empty:
        save_gdf(points, filenames['points'])
    else:
        logging.info("No point or multipoint layers to save.")

    if not lines.empty:
        save_gdf(lines, filenames['lines'])
    else:
        logging.info("No line or multiline layers to save.")

    if not polygons.empty:
        save_gdf(polygons, filenames['polygons'])
    else:
        logging.info("No polygon or multipolygon layers to save.")

    if not linear_rings.empty:
        save_gdf(linear_rings, filenames['linear_rings'])
    else:
        logging.info("No linear ring layers to save.")

    if not geometry_collections.empty:
        save_gdf(geometry_collections, filenames['geometry_collections'])
    else:
        logging.info("No geometry collection layers to save.")


def save_empty_layers(empty_layers: List[str], output_dir: str) -> None:
    """
    Save the list of empty layers to a file.
    :param empty_layers: List of empty layer names.
    :param output_dir: Directory where the file will be saved.
    """
    if empty_layers:
        with open(os.path.join(output_dir, "empty_layers.txt"), "w") as f:
            f.write("\n".join(empty_layers))
        logging.info("Saved empty layers list to 'empty_layers.txt'.")
