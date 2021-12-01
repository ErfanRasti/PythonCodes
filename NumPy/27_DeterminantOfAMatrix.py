# %%
"""In this code we wanna calculate determinant of matrix."""
import numpy as np
# %%
help(np.linalg.det)
# %%
a = np.arange(1, 5).reshape((2, 2))
a
# %%
np.linalg.det(a)
# %%
round(np.linalg.det(a))
# %%
b = np.arange(1, 10).reshape((3, 3))
b
# %%
np.linalg.det(b)
# %%
round(np.linalg.det(b))
