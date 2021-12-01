# %%
"""."""
import numpy as np
# %%
"""1. Integer Indexing"""
a = np.arange(1, 10)
a
# %%
"""Creating array of indices"""
indices = np.array([1, 4, 5])
# %%
"""Using indices array as index"""
a[indices]
# %%
a[[1, 4, 5]]
# %%
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b
# %%
b[[0, 2], [2, 0]]
# %%
b[[[1, 1, 2], [0, 2, 1]]]
# %%
a = np.arange(1, 10)
a
# %%
a[[1, 4, 1, 4, 1, 4]]
# %%
"""2. Boolean Indexing"""
a = np.array([[1, -2, 3], [4, -2, 3]])
a
# %%
a[a < 0]
# %%
a[a > 0]
# %%
a = np.array([[1, 2, -3], [-10, 20, 30], [3, -4, 4]])
a
# %%
a[a < 0]*2
# %%
