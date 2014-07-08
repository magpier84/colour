#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**data_structures.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines **Colour** package data structures objects.

**Others:**

"""

from __future__ import unicode_literals

import foundations.data_structures

import colour.utilities.verbose

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2013 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["Structure"]

LOGGER = colour.utilities.verbose.install_logger()

Structure = foundations.data_structures.Structure