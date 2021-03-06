# -*- coding: utf-8 -*-

import logging
import os


log = logging.getLogger("frkl")

"""Top-level package for tingex."""

__author__ = """Markus Binsteiner"""
__email__ = "markus@frkl.io"


def get_version():
    from pkg_resources import DistributionNotFound, get_distribution

    try:
        # Change here if project is renamed and does not equal the package name
        dist_name = __name__
        __version__ = get_distribution(dist_name).version
    except DistributionNotFound:

        try:
            version_file = os.path.join(os.path.dirname(__file__), "version.txt")

            if os.path.exists(version_file):
                with open(version_file, encoding="utf-8") as vf:
                    __version__ = vf.read()
            else:
                __version__ = "unknown"

        except (Exception):
            pass

        if __version__ is None:
            __version__ = "unknown"

    return __version__


try:
    from frkl.project_meta.app_environment import AppEnvironment

    TINGEX: AppEnvironment = AppEnvironment(main_module="tingex")
except Exception as e:
    log.debug(
        f"Can't create AppEnvironment (probably pkg 'frkl.project_meta' not in virtualenv): {e}"
    )
    TINGEX = None  # type: ignore
