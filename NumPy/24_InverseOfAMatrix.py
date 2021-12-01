# %%
"""In this code we wanna calculate the inverse of a matrix in numpy."""
import numpy as np
# %%
a = np.arange(1, 5).reshape((2, 2))
a
# %%
b = np.linalg.inv(a)
# %%
a.dot(b)
# %%
help(np.allclose)
# %%
np.eye(2)
# %%
np.allclose(a.dot(b), np.eye(2))
# %%
c = np.array([1, 2, 3, 4])
c
"""
"np.linalg.inv(c) will raise an error. for inversing a matrix in
it should be at least 2d.
"""
# %%
help(np.linalg.inv)
# %%
help(np.allclose)
