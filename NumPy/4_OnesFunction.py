# %%
"""Look."""
import numpy as np
# %%
"""
ones(shape, dtype=None, order='C')
    Return a new array of given shape and type, filled with ones.

    Parameters
    ----------
    shape : int or sequence of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    dtype : data-type, optional
        The desired data-type for the array, e.g., `numpy.int8`.  Default is
        `numpy.float64`.
    order : {'C', 'F'}, optional, default: C
        Whether to store multi-dimensional data in row-major
        (C-style) or column-major (Fortran-style) order in
        memory.

    Returns
    -------
    out : ndarray
        Array of ones with the given shape, dtype, and order.
"""
help(np.ones)
# %%
np.ones(8)
# %%
np.ones(7, dtype="complex")
# %%
np.ones((3, 4))
# %%
