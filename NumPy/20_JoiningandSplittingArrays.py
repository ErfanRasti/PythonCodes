# %%
"""We wanna get familiar with array manipulation(File 17-21)."""
import numpy as np
# %%
help(np.concatenate)
# %%
a = np.arange(1, 5)
b = np.arange(6)
c = np.arange(4)
# %%
np.concatenate((a, b))
# %%
np.concatenate((a, b, c))
# %%
c = np.zeros(10)
# %%
np.concatenate((a, b), out=c)
# %%
c = np.concatenate((a, b))
c
# %%
"""Both should be the same dimension."""
a = np.arange(1, 5).reshape(2, 2)
b = np.arange(5, 7).reshape(1, 2)
# %%
np.concatenate((a, b))
# %%
"""
np.concatenate((a, b), axis=1) will raise an error.

ValueError:
all the input array dimensions for the concatenation axis
must match exactly, but along dimension 0, the array at index 0
has size 2 and the array at index 1 has size 1
"""
np.concatenate((a, b.T), axis=1)
# %%
a = np.arange(5)
b = np.arange(1, 5).reshape(2, 2)
"""np.concatenate((a, b)) will raise an error."""
# %%
"""vstack vertical stack"""
help(np.vstack)
# %%
a = np.arange(6)
n = np.arange(5)
c = np.arange(5)+1
# %%
"""np.vstack((a, n)) will raise an error."""
np.vstack((n, c))
# %%
np.vstack((c, n))
# %%
a = np.arange(1, 5).reshape(2, 2)
b = np.arange(5, 7).reshape(1, 2)
# %%
np.concatenate((a, b))
# %%
np.vstack((a, b))
# %%
"""hstack horizontal stack"""
help(np.hstack)
# %%
a = np.arange(6)
n = np.arange(5)
c = np.arange(5)+1
# %%
# %%
np.hstack((a, n))
# %%
a = np.arange(1, 5).reshape(2, 2)
b = np.arange(5, 7).reshape(1, 2)
# %%
np.hstack((a, b.T))
# %%
help(np.split)
# %%
a = np.arange(1, 10)
# %%
"""np.split(a, 4) will raise an error."""
np.split(a, 3)
# %%
a = np.arange(1, 13).reshape(6, 2)
a
# %%
np.split(a, 2)
# %%
help(np.hsplit)
# %%
help(np.vsplit)
# %%
np.vsplit(a, 2)
# %%
a = np.arange(1, 13).reshape(2, 6)
a
# %%
np.hsplit(a, 3)
# %%
np.split(a, 3, axis=1)
# %%
