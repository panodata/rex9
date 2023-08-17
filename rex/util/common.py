# Copyright (c) 2023, The Panodata developers and contributors.
# Distributed under the terms of the AGPLv3 license, see LICENSE.

import logging
import sys

import colorlog
from colorlog.escape_codes import escape_codes

logger = logging.getLogger(__name__)


SQLALCHEMY_LOGGING = True


def setup_logging_basic(level=logging.INFO):
    log_format = "%(asctime)-15s [%(name)-18s] %(levelname)-8s: %(message)s"
    logging.basicConfig(format=log_format, stream=sys.stderr, level=level)


def setup_logging(level=logging.INFO):
    reset = escape_codes["reset"]
    log_format = f"%(asctime)-15s [%(name)-18s] %(log_color)s%(levelname)-8s:{reset} %(message)s"

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(log_format))

    logging.basicConfig(format=log_format, level=level, handlers=[handler])

    # Enable SQLAlchemy logging.
    if SQLALCHEMY_LOGGING:
        logging.getLogger("sqlalchemy").setLevel(level)


def get_version(appname):
    from importlib.metadata import PackageNotFoundError, version  # noqa

    try:
        return version(appname)
    except PackageNotFoundError:  # pragma: no cover
        return "unknown"
