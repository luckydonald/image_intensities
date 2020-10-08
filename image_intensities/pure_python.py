#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convert the image into the yuv colorspace, drop the u and v components,
and then average the y component over 4 evenly-spaced rectangles on the
image dimensions that gives you a floating point number
"""

from typing import Tuple, List, Union

from PIL import Image
from luckydonaldUtils.logger import logging

__author__ = 'luckydonald'


logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if


class RGB(object):
    r: int
    g: int
    b: int

    def __init__(
        self,
        r: int = 0,
        g: int = 0,
        b: int = 0,
    ):
        self.r = r
        self.g = g
        self.b = b
    # end def

    def __repr__(self):
        return f"{self.__class__.__name__}(r={self.r!r}, g={self.g!r}, b={self.b!r})"
    # end def
# end class


class Sums(object):
    nw: RGB
    ne: RGB
    sw: RGB
    se: RGB

    # noinspection PyShadowingNames
    def __init__(
        self,
        nw: Union[None, RGB] = None,
        ne: Union[None, RGB] = None,
        sw: Union[None, RGB] = None,
        se: Union[None, RGB] = None,
    ):
        if nw is None:
            nw = RGB()
        # end if
        self.nw = nw
        if ne is None:
            ne = RGB()
        # end if
        self.ne = ne
        if sw is None:
            sw = RGB()
        # end if
        self.sw = sw
        if se is None:
            se = RGB()
        # end if
        self.se = se
    # end def

    def __repr__(self):
        return f"{self.__class__.__name__}(nw={self.nw!r}, ne={self.ne!r}, sw={self.sw!r}, se={self.se!r})"
    # end def
# end class


class Luma(object):
    nw: float
    ne: float
    sw: float
    se: float

    def __init__(self, nw: float, ne: float, sw: float, se: float):
        self.nw = nw
        self.ne = ne
        self.sw = sw
        self.se = se

    # end def

    def __repr__(self):
        return f"{self.__class__.__name__}(nw={self.nw!r}, ne={self.ne!r}, sw={self.sw!r}, se={self.se!r})"
    # end def
# end class


def rgb_sums(img: Image.Image, log_prefix="") -> Sums:
    width, height = img.size
    pixels = list(img.getdata())
    sums = Sums()
    log_counter = -1  # more efficient then i % 10 == 0
    for i in range(height):
        log_counter += 1
        if log_counter == 10:
            logger.debug(f'{log_prefix}Processing line {i} of {width}x{height} px image.')
            log_counter = 0
        # end if
        for j in range(width):
            nw = (i <= height / 2) and (j <= width / 2)
            # noinspection PyShadowingNames
            ne = (i <= height / 2) and (j >= width / 2)
            # noinspection PyShadowingNames
            sw = (i >= height / 2) and (j <= width / 2)
            # noinspection PyShadowingNames
            se = (i >= height / 2) and (j >= width / 2)
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
def _calculate_luma(dim: int, sum: RGB):
    return (
       (sum.r / dim * 0.2126) +
       (sum.g / dim * 0.7152) +
       (sum.b / dim * 0.0772)
    ) / 3.0
# end def


def sums_to_luma(sums: Sums, img: Image.Image) -> Luma:
    width, height = img.size

    dim = max(width * height / 4.0, 1)

    return Luma(
        nw=_calculate_luma(dim, sums.nw),
        ne=_calculate_luma(dim, sums.ne),
        sw=_calculate_luma(dim, sums.sw),
        se=_calculate_luma(dim, sums.se),
    )
# end def


def rgb_luma_from_filename(filename: str) -> Luma:
    from PIL.Image import open
    img = open(filename)
    result = rgb_sums(img)
    return sums_to_luma(result, img)
# end def
