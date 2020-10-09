"""
The “out-of-line”, “API mode” gives you the most flexibility and speed to access a C library at the level of C, instead of at the binary level:
"""
# in a separate file "package/foo_build.py"

import cffi


ffibuilder = cffi.FFI()
ffibuilder.set_source(
    module_name="image_intensities._native_code._image_intensities",
    source="""
    #include "definitions.h"
    #include "turbojpeg.h"
    """,
    include_dirs=[  # -I
        "./image_intensities/_native_code/turbojpeg",
        "./image_intensities/_native_code"
    ],
    libraries=[  # -L
        "./image_intensities/_native_code/jpeg",
        "./image_intensities/_native_code/png",
    ],
    sources=[
         "./image_intensities/_native_code/turbojpeg/jsimd_none.c",
         "./image_intensities/_native_code/turbojpeg/jchuff.c",
         "./image_intensities/_native_code/turbojpeg/jcapimin.c",
         "./image_intensities/_native_code/turbojpeg/jcapistd.c",
         "./image_intensities/_native_code/turbojpeg/jccolor.c",
         "./image_intensities/_native_code/turbojpeg/jcicc.c",
         "./image_intensities/_native_code/turbojpeg/jccoefct.c",
         "./image_intensities/_native_code/turbojpeg/jcinit.c",
         "./image_intensities/_native_code/turbojpeg/jcdctmgr.c",
         "./image_intensities/_native_code/turbojpeg/jcmainct.c",
         "./image_intensities/_native_code/turbojpeg/jcmarker.c",
         "./image_intensities/_native_code/turbojpeg/jcmaster.c",
         "./image_intensities/_native_code/turbojpeg/jcomapi.c",
         "./image_intensities/_native_code/turbojpeg/jcparam.c",
         "./image_intensities/_native_code/turbojpeg/jcphuff.c",
         "./image_intensities/_native_code/turbojpeg/jcprepct.c",
         "./image_intensities/_native_code/turbojpeg/jcsample.c",
         "./image_intensities/_native_code/turbojpeg/jctrans.c",
         "./image_intensities/_native_code/turbojpeg/jdapimin.c",
         "./image_intensities/_native_code/turbojpeg/jdapistd.c",
         "./image_intensities/_native_code/turbojpeg/jdatadst.c",
         "./image_intensities/_native_code/turbojpeg/jdatasrc.c",
         "./image_intensities/_native_code/turbojpeg/jdcoefct.c",
         "./image_intensities/_native_code/turbojpeg/jdcolor.c",
         "./image_intensities/_native_code/turbojpeg/jddctmgr.c",
         "./image_intensities/_native_code/turbojpeg/jdhuff.c",
         "./image_intensities/_native_code/turbojpeg/jdicc.c",
         "./image_intensities/_native_code/turbojpeg/jdinput.c",
         "./image_intensities/_native_code/turbojpeg/jdmainct.c",
         "./image_intensities/_native_code/turbojpeg/jdmarker.c",
         "./image_intensities/_native_code/turbojpeg/jdmaster.c",
         "./image_intensities/_native_code/turbojpeg/jdmerge.c",
         "./image_intensities/_native_code/turbojpeg/jdphuff.c",
         "./image_intensities/_native_code/turbojpeg/jdpostct.c",
         "./image_intensities/_native_code/turbojpeg/jdsample.c",
         "./image_intensities/_native_code/turbojpeg/jdtrans.c",
         "./image_intensities/_native_code/turbojpeg/jerror.c",
         "./image_intensities/_native_code/turbojpeg/jfdctflt.c",
         "./image_intensities/_native_code/turbojpeg/jfdctfst.c",
         "./image_intensities/_native_code/turbojpeg/jfdctint.c",
         "./image_intensities/_native_code/turbojpeg/jidctflt.c",
         "./image_intensities/_native_code/turbojpeg/jidctfst.c",
         "./image_intensities/_native_code/turbojpeg/jidctint.c",
         "./image_intensities/_native_code/turbojpeg/jidctred.c",
         "./image_intensities/_native_code/turbojpeg/jquant1.c",
         "./image_intensities/_native_code/turbojpeg/jquant2.c",
         "./image_intensities/_native_code/turbojpeg/jutils.c",
         "./image_intensities/_native_code/turbojpeg/jmemmgr.c",
         "./image_intensities/_native_code/turbojpeg/jmemnobs.c",
         "./image_intensities/_native_code/turbojpeg/jaricom.c",
         "./image_intensities/_native_code/turbojpeg/jdarith.c",
         "./image_intensities/_native_code/turbojpeg/jcarith.c",
         "./image_intensities/_native_code/turbojpeg/turbojpeg.c",
         "./image_intensities/_native_code/turbojpeg/transupp.c",
         "./image_intensities/_native_code/turbojpeg/jdatadst-tj.c",
         "./image_intensities/_native_code/turbojpeg/jdatasrc-tj.c",
         "./image_intensities/_native_code/turbojpeg/rdbmp.c",
         "./image_intensities/_native_code/turbojpeg/rdppm.c",
         "./image_intensities/_native_code/turbojpeg/wrbmp.c",
         "./image_intensities/_native_code/turbojpeg/wrppm.c",

         "./image_intensities/_native_code/main/intensities.c",
         "./image_intensities/_native_code/main/png.c",
         "./image_intensities/_native_code/main/jpeg.c",
     ],
    extra_compile_args=[
        "-std=c99",
        "-fPIC",
        "-O3",
        "-DPPM_SUPPORTED",
        "-DBMP_SUPPORTED",
    ],
)
ffibuilder.cdef("""
    struct intensity_data {
        double nw;
        double ne;
        double sw;
        double se;
        int error;
    };

    struct intensity_data lib_jpeg_intensities(const char *file_name);
    struct intensity_data png_intensities(const char *file_name);
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
# end if
