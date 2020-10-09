from mimetypes import guess_type

from cffi import FFI
from luckydonaldUtils.encoding import to_binary as b

from .pure_python import Luma


def convert_struct_to_luma(struct) -> Luma:
    return Luma(nw=struct.nw, ne=struct.ne, sw=struct.sw, se=struct.se)
# end def


def lib_jpeg_intensities(filename: str, lib: FFI) -> Luma:
    # noinspection PyUnresolvedReferences
    return convert_struct_to_luma(lib.jpeg_intensities(b(filename)))
# end def


def lib_png_intensities(filename: str, lib: FFI) -> Luma:
    # noinspection PyUnresolvedReferences
    return convert_struct_to_luma(lib.png_intensities(b(filename)))
# end def


def lib_rgb_luma_from_filename(filename, lib):
    (mime_type, encoding) = guess_type(filename)
    if mime_type == 'image/png':
        return lib_png_intensities(filename, lib)
    elif mime_type == 'image/jpeg':
        return lib_jpeg_intensities(filename, lib)
    else:
        raise ValueError('Unknown mime.')
    # end if
# end def
