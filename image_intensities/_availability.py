#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if

AVAILABLE_BACKENDS = {
    "pure_python": True,
    "compiled_cython": None,
    "compiled_cffi": None,
    "native_cffi": None,
}

try:
    from image_intensities.compiled_cython import rgb_sums, sums_to_luma, rgb_luma_from_filename
    AVAILABLE_BACKENDS["compiled_cython"] = True
except ImportError as e:
    AVAILABLE_BACKENDS["compiled_cython"] = False
    print(f'compiled_cython failed: {e!s}')
# end try

try:
    from image_intensities.compiled_cffi import jpeg_intensities, png_intensities, rgb_luma_from_filename
    AVAILABLE_BACKENDS["compiled_cffi"] = True
except ImportError as e:
    AVAILABLE_BACKENDS["compiled_cffi"] = False
    print(f'compiled_cffi failed: {e!s}')
# end try

try:
    from image_intensities.native_cffi import jpeg_intensities, png_intensities, rgb_luma_from_filename
    AVAILABLE_BACKENDS["native_cffi"] = True
except ImportError as e:
    AVAILABLE_BACKENDS["native_cffi"] = False
    print(f'native_cffi failed: {e!s}')
# end try

