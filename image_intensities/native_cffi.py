from .pure_python import Luma
from .shared_cffi import lib_jpeg_intensities, lib_png_intensities, lib_rgb_luma_from_filename

# noinspection PyProtectedMember,PyUnresolvedReferences
from ._native_code._image_intensities import ffi, lib


def jpeg_intensities(filename) -> Luma:
    return lib_jpeg_intensities(filename, lib)
# end def


def png_intensities(filename) -> Luma:
    return lib_png_intensities(filename, lib)
# end def


def rgb_luma_from_filename(filename) -> Luma:
    return lib_rgb_luma_from_filename(filename, lib)
# end def
