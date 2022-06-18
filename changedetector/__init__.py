"""
CHANGE DETECTOR
~~~~~~~~~~~~~~~
A basic change detector for the Python, Ruby and C++.
:copyright (c) 2022 LuxLuth
:license: MIT, see LICENSE for more details.
"""
import os

__title__ = 'changedetector'
__author__ = 'LuxLuth'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2022 LuxLuth'
__version__ = '0.0.1'

# The directory where the package is imported in.
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from .detectchange import *
