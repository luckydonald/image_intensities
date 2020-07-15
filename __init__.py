#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if

from .pure_python import RGB, Luma, Sums

try:
    from .compiled_cython import rgb_sums, sums_to_luma
except ImportError:
    from .pure_python import rgb_sums, sums_to_luma
# except

