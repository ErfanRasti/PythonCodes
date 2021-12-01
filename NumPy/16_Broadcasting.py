# %%
"""
Broadcasting is very important.

For more information check this site:
https://numpy.org/doc/stable/user/theory.broadcasting.html#array-broadcasting-in-numpy
"""
import numpy as np
# %%
a = np.array([10, 20, 30])
b = np.array([1, 2, 3, 4])
# %%
a.shape
# %%
b.shape
# %%
"""
a+b
It will raise an error.
ValueError:
operands could not be broadcast together
with shapes (3,) (4,)
"""
# %%
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([1, 2, 3])
c = np.array([10, 20])
# %%
a+c
# %%
"""a+b will rise an error."""
a.shape
# %%
b.shape
# %%
a = np.array([[1], [2], [3]])
b = np.array([1, 2, 3])
# %%
a.shape
# %%
b.shape
# %%
a+b
# %%
