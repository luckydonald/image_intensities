#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mimetypes import guess_type

from luckydonaldUtils.encoding import to_binary as b
from luckydonaldUtils.logger import logging

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if

from cffi import FFI
from os import path
from .pure_python import Luma

so_file = path.abspath(__file__ + "/../image_intensities/lib/libimage_intensities.so")
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


def jpeg_intensities(filename):
    struct = lib.jpeg_intensities(b(filename))
    return Luma(nw=struct.nw, ne=struct.ne, sw=struct.sw, se=struct.se)
# end def


def png_intensities(filename):
    struct = lib.png_intensities(b(filename))
    return Luma(nw=struct.nw, ne=struct.ne, sw=struct.sw, se=struct.se)
# end def


def rgb_luma_from_filename(filename):
    (mime_type, encoding) = guess_type(filename)
    if mime_type == 'image/png':
        return png_intensities(filename)
    elif mime_type == 'image/jpeg':
        return jpeg_intensities(filename)
    else:
        raise ValueError('Unknown mime.')
    # end if
# end def
