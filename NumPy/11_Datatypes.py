# %%
"""
In this code we wanna get familiar with numpy datatypes.

For more information check this link:
https://numpy.org/doc/stable/reference/arrays.dtypes.html
"""
import numpy as np
# %%
a = np.zeros(5)
a.dtype
# %%
b = np.zeros(6, dtype=np.int8)
b
# %%
"""Built-in Python types"""
c = np.zeros(6, dtype=int)
c.dtype
# %%
"""Using datatype as a method"""
x = np.float32(1)
x
# %%
x.dtype
# %%
"""Array-protocol type strings"""
a = np.array([1, 2, 3], dtype='f')
a
# %%
a = np.zeros(3)
a
# %%
"""Changing Datatype"""
a.astype(int)
# %%
np.float64(a)
# %%
a.dtype
# %%
