# %%
"""In this code we wanna solve a linear equation."""
import numpy as np
# %%
"""We wanna solve this system of equations:
3x + y = 9
x + 2y = 8
"""
a = np.array([[3, 1], [1, 2]])
a
b = np.array([9, 8])
b
# %%
np.linalg.solve(a, b)
# %%
b = np.array([9, 8]).reshape((-1, 1))
b
# %%
"""The shape of output array will be the same as b."""
np.linalg.solve(a, b)
