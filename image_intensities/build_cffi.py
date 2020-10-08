"""
The “out-of-line”, “API mode” gives you the most flexibility and speed to access a C library at the level of C, instead of at the binary level:
"""
# in a separate file "package/foo_build.py"

import cffi


ffibuilder = cffi.FFI()
ffibuilder.set_source(
    module_name="image_intensities._foo",
    source="""
    #include "definitions.h"
    #include "turbojpeg.h"
    """,
    #define_macros=[("HAVE_UNSIGNED_CHAR", "1")],
    include_dirs=[  # -I
        "image_intensities/turbojpeg"
    ],
    libraries=[  # -L
        "turbojpeg", "jpeg", "png"
    ],
    extra_objects=[
        "turbojpeg/jsimd_none",
        "turbojpeg/jchuff",
        "turbojpeg/jcapimin",
        "turbojpeg/jcapistd",
        "turbojpeg/jccolor",
        "turbojpeg/jcicc",
        "turbojpeg/jccoefct",
        "turbojpeg/jcinit",
        "turbojpeg/jcdctmgr",
        "turbojpeg/jcmainct",
        "turbojpeg/jcmarker",
        "turbojpeg/jcmaster",
        "turbojpeg/jcomapi",
        "turbojpeg/jcparam",
        "turbojpeg/jcphuff",
        "turbojpeg/jcprepct",
        "turbojpeg/jcsample",
        "turbojpeg/jctrans",
        "turbojpeg/jdapimin",
        "turbojpeg/jdapistd",
        "turbojpeg/jdatadst",
        "turbojpeg/jdatasrc",
        "turbojpeg/jdcoefct",
        "turbojpeg/jdcolor",
        "turbojpeg/jddctmgr",
        "turbojpeg/jdhuff",
        "turbojpeg/jdicc",
        "turbojpeg/jdinput",
        "turbojpeg/jdmainct",
        "turbojpeg/jdmarker",
        "turbojpeg/jdmaster",
        "turbojpeg/jdmerge",
        "turbojpeg/jdphuff",
        "turbojpeg/jdpostct",
        "turbojpeg/jdsample",
        "turbojpeg/jdtrans",
        "turbojpeg/jerror",
        "turbojpeg/jfdctflt",
        "turbojpeg/jfdctfst",
        "turbojpeg/jfdctint",
        "turbojpeg/jidctflt",
        "turbojpeg/jidctfst",
        "turbojpeg/jidctint",
        "turbojpeg/jidctred",
        "turbojpeg/jquant1",
        "turbojpeg/jquant2",
        "turbojpeg/jutils",
        "turbojpeg/jmemmgr",
        "turbojpeg/jmemnobs",
        "turbojpeg/jaricom",
        "turbojpeg/jdarith",
        "turbojpeg/jcarith",
        "turbojpeg/turbojpeg",
        "turbojpeg/transupp",
        "turbojpeg/jdatadst-tj",
        "turbojpeg/jdatasrc-tj",
        "turbojpeg/rdbmp",
        "turbojpeg/rdppm",
        "turbojpeg/wrbmp",
        "turbojpeg/wrppm",
    ],
    extra_compile_args=[
        "-std=c99",
        "-fPIC",
        "-shared",
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

    struct intensity_data jpeg_intensities(const char *file_name);
    struct intensity_data png_intensities(const char *file_name);
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
# end if
