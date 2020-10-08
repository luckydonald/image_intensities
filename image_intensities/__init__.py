#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if

__version__ = '0.0.1'
VERSION = __version__

from .pure_python import RGB, Luma, Sums

try:
    from .compiled_cython import rgb_sums, sums_to_luma
except ImportError:
    from .pure_python import rgb_sums, sums_to_luma
# except

try:
    from .compiled_cffi import jpeg_intensities, png_intensities, rgb_luma_from_filename
except ImportError:
    try:
        from .compiled_cython import rgb_luma_from_filename
    except ImportError:
        from .pure_python import rgb_luma_from_filename
    # except
# end try



