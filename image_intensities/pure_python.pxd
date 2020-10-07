cdef class RGB:
    cpdef public int r, g, b
# end class

cdef class Sums:
    cpdef public RGB nw, ne, sw, se
# end class

cdef class Luma:
    cpdef public float nw, ne, sw, se
    # def public unicode __repr__(self)
# end class
