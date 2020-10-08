"""
The “out-of-line”, “API mode” gives you the most flexibility and speed to access a C library at the level of C, instead of at the binary level:
"""
# in a separate file "package/foo_build.py"

import cffi


ffibuilder = cffi.FFI()
ffibuilder.set_source(
    module_name="_native",
    source="""
    #include "definitions.h"
    #include "turbojpeg.h"
    """,
    #define_macros=[("HAVE_UNSIGNED_CHAR", "1")],
    include_dirs=[  # -I
        "turbojpeg",
    ],
    libraries=[  # -L
        "jpeg", "png", #"intensities"
    ],
    sources=[
         "turbojpeg/jsimd_none.c",
         "turbojpeg/jchuff.c",
         "turbojpeg/jcapimin.c",
         "turbojpeg/jcapistd.c",
         "turbojpeg/jccolor.c",
         "turbojpeg/jcicc.c",
         "turbojpeg/jccoefct.c",
         "turbojpeg/jcinit.c",
         "turbojpeg/jcdctmgr.c",
         "turbojpeg/jcmainct.c",
         "turbojpeg/jcmarker.c",
         "turbojpeg/jcmaster.c",
         "turbojpeg/jcomapi.c",
         "turbojpeg/jcparam.c",
         "turbojpeg/jcphuff.c",
         "turbojpeg/jcprepct.c",
         "turbojpeg/jcsample.c",
         "turbojpeg/jctrans.c",
         "turbojpeg/jdapimin.c",
         "turbojpeg/jdapistd.c",
         "turbojpeg/jdatadst.c",
         "turbojpeg/jdatasrc.c",
         "turbojpeg/jdcoefct.c",
         "turbojpeg/jdcolor.c",
         "turbojpeg/jddctmgr.c",
         "turbojpeg/jdhuff.c",
         "turbojpeg/jdicc.c",
         "turbojpeg/jdinput.c",
         "turbojpeg/jdmainct.c",
         "turbojpeg/jdmarker.c",
         "turbojpeg/jdmaster.c",
         "turbojpeg/jdmerge.c",
         "turbojpeg/jdphuff.c",
         "turbojpeg/jdpostct.c",
         "turbojpeg/jdsample.c",
         "turbojpeg/jdtrans.c",
         "turbojpeg/jerror.c",
         "turbojpeg/jfdctflt.c",
         "turbojpeg/jfdctfst.c",
         "turbojpeg/jfdctint.c",
         "turbojpeg/jidctflt.c",
         "turbojpeg/jidctfst.c",
         "turbojpeg/jidctint.c",
         "turbojpeg/jidctred.c",
         "turbojpeg/jquant1.c",
         "turbojpeg/jquant2.c",
         "turbojpeg/jutils.c",
         "turbojpeg/jmemmgr.c",
         "turbojpeg/jmemnobs.c",
         "turbojpeg/jaricom.c",
         "turbojpeg/jdarith.c",
         "turbojpeg/jcarith.c",
         "turbojpeg/turbojpeg.c",
         "turbojpeg/transupp.c",
         "turbojpeg/jdatadst-tj.c",
         "turbojpeg/jdatasrc-tj.c",
         "turbojpeg/rdbmp.c",
         "turbojpeg/rdppm.c",
         "turbojpeg/wrbmp.c",
         "turbojpeg/wrppm.c",
         "intensities.c", "png.c", "jpeg.c",
     ],
    extra_compile_args=[
        "-std=c99",
        "-fPIC",
        "-O3",
        "-shared",
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

    struct intensity_data jpeg_intensities(const char *file_name);
    struct intensity_data png_intensities(const char *file_name);
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
# end if
