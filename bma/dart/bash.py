#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from bma.paths import DATA_PATH
from bma.ABAMB import BARRRACUDA_C


def get_script(path):
    with open(os.path.join(DATA_PATH, path), "r") as script:
        return script.read()
