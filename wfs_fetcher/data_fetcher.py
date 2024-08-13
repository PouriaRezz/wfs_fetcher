#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by rezaei.pooriya99@gmail.com on 13.08.2024

from owslib.wfs import WebFeatureService
from typing import Tuple, List
import geopandas as gpd
from io import BytesIO
import logging


def fetch_features_for_layer(wfs: WebFeatureService, layer: str) -> Tuple[gpd.GeoDataFrame, bool]:
    """
    Fetch features for a single layer.
    :param wfs: Initialized WebFeatureService object.
    :param layer: Name of the layer to fetch data from.
    :return: Tuple containing GeoDataFrame with features and a boolean indicating if it was empty.
    """
    try:
        response = wfs.getfeature(typename=layer)
        response_content = response.read().strip()
        if not response_content:
            logging.info(f"No data returned for layer: {layer}")
            return gpd.GeoDataFrame(), True

        gdf = gpd.read_file(BytesIO(response_content))
        gdf['layer_name'] = layer
        return gdf, gdf.empty
    except Exception as e:
        logging.error(f"Error processing layer {layer}: {e}")
        return gpd.GeoDataFrame(), True


def fetch_layer_data(wfs: WebFeatureService, layers: List[str]) -> Tuple[List[gpd.GeoDataFrame], List[str]]:
    """
    Fetch and return features from all layers.
    :param wfs: Initialized WebFeatureService object.
    :param layers: List of layer names to fetch data from.
    :return: Tuple containing a list of GeoDataFrames with features and a list of empty layer names.
    """
    all_features = []
    empty_layers = []

    for layer in layers:
        logging.info(f"Fetching features for layer: {layer} with title: {wfs[layer].title}")
        gdf, is_empty = fetch_features_for_layer(wfs, layer)

        if is_empty:
            empty_layers.append(layer)
        else:
            all_features.append(gdf)

    return all_features, empty_layers
