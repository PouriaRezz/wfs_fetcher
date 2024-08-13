#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by rezaei.pooriya99@gmail.com on 13.08.2024

from owslib.wfs import WebFeatureService


def initialize_wfs_service(url: str, version: str = "2.0.0") -> WebFeatureService:
    """
    Initialize and return the WFS service.
    :param url: URL of the WFS service.
    :param version: WFS version to use.
    :return: Initialized WebFeatureService object.
    """
    return WebFeatureService(url=url, version=version)
