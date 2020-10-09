from timeit import timeit
import sys
FILENAME = sys.argv[1]

print('native_cffi')
result_native_cffi = None
try:
    from image_intensities.native_cffi import rgb_luma_from_filename as rgb_luma_from_filename_native_cffi
    result_native_cffi = timeit(lambda: rgb_luma_from_filename_native_cffi(filename=FILENAME), number=1)
    print(f'took {result_native_cffi}s.')
except ImportError:
    print('could not import native_cffi.')
# end try

print('compiled_cffi')
result_compiled_cffi = None
try:
    from image_intensities.compiled_cffi import rgb_luma_from_filename as rgb_luma_from_filename_compiled_cffi
    result_compiled_cffi = timeit(lambda: rgb_luma_from_filename_compiled_cffi(filename=FILENAME), number=1)
    print(f'took {result_compiled_cffi}s.')
except ImportError:
    print('could not import compiled_cffi.')
# end try

print('compiled_cython')
result_compiled_cython = None
try:
    from image_intensities.compiled_cython import rgb_luma_from_filename as rgb_luma_from_filename_compiled_cython
    result_compiled_cython = timeit(lambda: rgb_luma_from_filename_compiled_cython(filename=FILENAME), number=1)
    print(f'took {result_compiled_cython}s.')
except ImportError:
    print('could not import compiled_cython.')
# end try

print('pure_python')
result_pure_python = None
try:
    from image_intensities.pure_python import rgb_luma_from_filename as rgb_luma_from_filename_pure_python
    result_pure_python = timeit(lambda: rgb_luma_from_filename_pure_python(filename=FILENAME), number=1)
    print(f'took {result_pure_python}s.')
except ImportError:
    print('could not import pure_python.')
# end try



