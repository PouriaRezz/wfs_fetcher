#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by rezaei.pooriya99@gmail.com on 13.08.2024

import argparse
import logging
import geopandas as gpd
import pandas as pd
import sys

from .wfs_service import initialize_wfs_service
from .data_fetcher import fetch_layer_data
from .geometry_categorizer import categorize_geometries
from .file_exporter import save_geodataframes, save_empty_layers
from .logging_config import setup_logging


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.
    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Fetch and save features from a WFS service.")
    parser.add_argument(
        "--url",
        required=True,
        help="URL of the WFS service."
    )
    parser.add_argument(
        "--format",
        choices=["GeoJSON", "GeoPackage", "Shapefile"],
        default="GeoJSON",
        help="File format for saving GeoDataFrames (default: GeoJSON)."
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory to save the output files (default: 'output')."
    )
    return parser.parse_args()


def main() -> None:
    """
    Main function to initialize WFS service, fetch data, and save results in the specified format.
    """
    args = parse_args()
    setup_logging()
    logging.info(f"Arguments received: {args}")

    # Initialize WFS service
    try:
        wfs = initialize_wfs_service(args.url)
    except Exception as e:
        logging.error(f"Failed to initialize WFS service: {e}")
        sys.exit(1)

    # List of all layer names
    layers = list(wfs.contents.keys())
    logging.info(f"Available layers: {layers}")

    # Fetch features from all layers
    try:
        all_features, empty_layers = fetch_layer_data(wfs, layers)
    except Exception as e:
        logging.error(f"Failed to fetch data from WFS layers: {e}")
        sys.exit(1)

    # Combine all features into a single GeoDataFrame
    if all_features:
        combined_gdf = gpd.GeoDataFrame(pd.concat(all_features, ignore_index=True, sort=False))
    else:
        logging.info("No features were retrieved from any layer.")
        combined_gdf = gpd.GeoDataFrame()  # Empty GeoDataFrame

    # Categorize and save GeoDataFrames
    if not combined_gdf.empty:
        points, lines, polygons, linear_rings, geometry_collections = categorize_geometries(combined_gdf)
        save_geodataframes(points, lines, polygons, linear_rings, geometry_collections, args.output_dir, args.format)
    else:
        logging.info("Combined GeoDataFrame is empty. No data to categorize or save.")

    # Save the list of empty layers
    if empty_layers:
        save_empty_layers(empty_layers, args.output_dir)
    else:
        logging.info("No empty layers to save.")

    logging.info("Process completed successfully.")
    sys.exit(0)  # Exit with a success code


if __name__ == "__main__":
    main()
