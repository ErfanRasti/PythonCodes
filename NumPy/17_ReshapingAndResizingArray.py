# %%
"""We wanna get familiar with array manipulation(File 17-21)."""
import numpy as np
# %%
help(np.reshape)
# %%
a = np.arange(10)
# %%
a.shape
# %%
b = np.reshape(a, (5, 2))
# %%
b
# %%
b.shape
# %%
c = np.reshape(a, (5, 2), order="F")
# %%
c
# %%
"""
np.reshape(a,(4,3))
It will rise an error.
ValueError:
cannot reshape array of size 10 into shape (4,3)
"""
# %%
a.reshape((5, 2))
# %%
help(np.resize)
# %%
a = np.arange(5)
# %%
np.resize(a, (2, 3))
# %%
np.resize(a, (5, 2))
# %%
"""a.resize will change the original array."""
a.resize((5, 2))
# %%
a
# %%
