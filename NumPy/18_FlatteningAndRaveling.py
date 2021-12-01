# %%
"""We wanna get familiar with array manipulation(File 17-21)."""
import numpy as np
# %%
b = np.array([[[1, 2, 3, ], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]])
b
# %%
b.flatten()
# %%
b.flatten(order="F")
# %%
b.flatten(order="K")
# %%
b.flatten(order="A")
# %%
a = np.array([[1, 2], [3, 4]])
a
# %%
a.flatten()
# %%
a.flatten(order="F")
# %%
help(np.ravel)
# %%
a = np.array([[10, 20], [30, 40]])
a
# %%
np.ravel(a)
# %%
np.ravel(a, order="F")
# %%
np.ravel(b)
# %%
b.ravel()
# %%
"""
Differences:
np.flatten function will return the copy of the array but
np.ravel function will return only the reference or view of
of the original array and np.ravel will return the copy only it is needed.
np.flatten is only o method of the array but the
np.ravel is a library level function.
"""
# %%
