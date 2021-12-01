# %%
"""In this code we wanna introduce matrix in form of array in numpy."""
import numpy as np
# %%
a = np.arange(1, 5).reshape(2, 2)
a
b = np.arange(10, 41, 10).reshape(2, 2)
b
# %%
a+b
# %%
a*b
# %%
a.dot(b)
# %%
help(np.dot)
# %%
np.transpose(a)
# %%
a.T
# %%
a.transpose
