#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 00:56:37 2022

@author: josemi
"""

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("nd_naive.pyx")
)