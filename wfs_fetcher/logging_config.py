#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by rezaei.pooriya99@gmail.com on 13.08.2024

import logging


def setup_logging(level: int = logging.INFO) -> None:
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')
