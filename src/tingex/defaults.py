# -*- coding: utf-8 -*-
import os
import sys

from appdirs import AppDirs


tingex_app_dirs = AppDirs("tingex", "frkl")

if not hasattr(sys, "frozen"):
    TINGEX_MODULE_BASE_FOLDER = os.path.dirname(__file__)
    """Marker to indicate the base folder for the `tingex` module."""
else:
    TINGEX_MODULE_BASE_FOLDER = os.path.join(sys._MEIPASS, "tingex")  # type: ignore
    """Marker to indicate the base folder for the `tingex` module."""

TINGEX_RESOURCES_FOLDER = os.path.join(TINGEX_MODULE_BASE_FOLDER, "resources")
