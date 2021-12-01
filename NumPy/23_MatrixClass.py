# %%
"""In this code we wanna introdunce matrix class in numpy."""
import numpy as np
# %%
help(np.matrix)
# %%
a = np.matrix("1 2 3 4")
a
# %%
a = np.matrix("1 2;3 4")
a
# %%
b = np.matrix(np.arange(10, 41, 10).reshape(2, 2))
b
# %%
a*b
# %%
a.T
