# %%
"""Look you b****."""
import numpy as np
# %%
a = np.array([1, 2, 3, 4])
# %%
"""ndim gives us the dimension of array."""
a.ndim
# %%
b = np.array([[1, 2], [3, 4]])
# %%
b.ndim
# %%
a = np.zeros(5)
# %%
"""shape is a tuple of integers indicating the lengths of each dimensions."""
a.shape
# %%
b.shape
# %%
c = np.zeros((2, 3, 4))
# %%
c.shape
# %%
"""size indicates the number of elements in the array."""
c.size
# %%
b.size
# %%
"""dtype indicates the datatype of array's elements."""
c.dtype
# %%
b.dtype
# %%
"""itemsize is the size of each element size in bytes."""
c.itemsize
# %%
b.itemsize
# %%
