#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if


from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["image_intensities/compiled_cython.pyx", "image_intensities/pure_python.py", ])
)
