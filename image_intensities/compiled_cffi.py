#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from cffi import FFI
from luckydonaldUtils.logger import logging

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if

from pathlib import Path
from .pure_python import Luma
from .shared_cffi import lib_jpeg_intensities, lib_rgb_luma_from_filename
from .shared_cffi import lib_png_intensities

so_files = Path(__file__).joinpath('..', '_native_code').absolute().glob("_image_intensities{,.*}.so")
try:
    so_file = str(next(so_files))
except StopIteration:
    logger.warning('Loading optimized library via CFFI failed, file not found.')
    raise ImportError('File not found.')
# end if
ffi = FFI()
ffi.cdef("""
    extern struct intensity_data {
        double nw;
        double ne;
        double sw;
        double se;
        int error;
    } intensity_data;

    struct intensity_data jpeg_intensities(const char *file_name);
    struct intensity_data png_intensities(const char *file_name);
""")
try:
    lib = ffi.dlopen(so_file)
except OSError as e:
    logger.warning('Loading optimized library via CFFI failed:', exc_info=True)
    raise ImportError('OSError: ' + str(e))
# end if


def jpeg_intensities(filename) -> Luma:
    return lib_jpeg_intensities(filename, lib)
# end def


def png_intensities(filename) -> Luma:
    return lib_png_intensities(filename, lib)
# end def


def rgb_luma_from_filename(filename) -> Luma:
    return lib_rgb_luma_from_filename(filename, lib)
# end def
