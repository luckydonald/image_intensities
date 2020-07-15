#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convert the image into the yuv colorspace, drop the u and v components,
and then average the y component over 4 evenly-spaced rectangles on the
image dimensions that gives you a floating point number
"""

from typing import Union

from PIL import Image
from luckydonaldUtils.logger import logging
from libc.stdint cimport uint32_t

from .pure_python import RGB, Sums, Luma

__author__ = 'luckydonald'


logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if


cdef rgb_sums(Image.Image img: Image.Image, log_prefix = "") -> Sums:
    cdef uint32_t width, height

    width, height = img.size
    pixels = list(img.getdata())
    sums = Sums()

    for i in range(height):
        if i % 10 == 0:
            logger.debug(f'{log_prefix}Processing line {i} of {width}x{height} px image.')
        # end if
        for j in range(width):
            cdef int nw = (i <= height / 2) and (j <= width / 2)
            # noinspection PyShadowingNames
            cdef int ne = (i <= height / 2) and (j >= width / 2)
            # noinspection PyShadowingNames
            cdef int sw = (i >= height / 2) and (j <= width / 2)
            # noinspection PyShadowingNames
            cdef int se = (i >= height / 2) and (j >= width / 2)

            img.load()
            pixel = pixels[i * width + j]
            r, g, b = pixel[0], pixel[1], pixel[2]

            if nw:
                sums.nw.r += r
                sums.nw.g += g
                sums.nw.b += b
            # end if

            if ne:
                sums.ne.r += r
                sums.ne.g += g
                sums.ne.b += b
            # end if

            if sw:
                sums.sw.r += r
                sums.sw.g += g
                sums.sw.b += b
            # end if

            if se:
                sums.se.r += r
                sums.se.g += g
                sums.se.b += b
            # end if
        # end for
    # end for
    return sums
# end def


# noinspection PyShadowingBuiltins
def calculate_luma(double dim: int, sum: RGB):
    return (
       (sum.r / dim * 0.2126) +
       (sum.g / dim * 0.7152) +
       (sum.b / dim * 0.0772)
    ) / 3.0
# end def


cdef sums_to_luma(sums: Sums, img: Image.Image) -> Luma:
    cdef uint32_t width, height
    width, height = img.size

    cdef double dim = max(width * height / 4.0, 1)

    return Luma(
        nw=calculate_luma(dim, sums.nw),
        ne=calculate_luma(dim, sums.ne),
        sw=calculate_luma(dim, sums.sw),
        se=calculate_luma(dim, sums.se),
    )
# end def
