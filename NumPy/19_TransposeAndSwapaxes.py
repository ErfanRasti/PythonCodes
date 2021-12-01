# %%
"""We wanna get familiar with array manipulation(File 17-21)."""
import numpy as np
# %%
help(np.transpose)
# %%
array1 = np.arange(1, 11).reshape(5, 2)
array1
# %%
np.transpose(array1)
# %%
array1.shape
# %%
np.transpose(array1).shape
# %%
a = np.arange(1, 25).reshape(2, 3, 4)
a
# %%
np.transpose(a)
# %%
np.transpose(a).shape
# %%
a = np.arange(1, 10)
a
# %%
np.transpose(a)
# %%
np.transpose(array1, axes=(1, 0))
# %%
np.transpose(array1, axes=(0, 1))
# %%
a = np.arange(1, 25).reshape(2, 3, 4)
a
# %%
"""
In the a we had:
axis 0: 2
axis 1: 3
axis 2: 4
Now we wanna reshape the 3d array to (3, 4, 2).
"""
np.transpose(a, axes=(1, 2, 0))
# %%
a.transpose()
# %%
a.T
# %%
help(np.swapaxes)
# %%
"""
Swap the first and second array.
The new shape will be (3, 2, 4)/
"""
np.swapaxes(a, 0, 1)
# %%
a = np.arange(1, 5).reshape(2, 2)
a
# %%
np.swapaxes(a, 0, 1)
# %%
np.swapaxes(a, 1, 0)
# %%
a = np.array([[1, 2, 3]])
a
# %%
a.shape
# %%
a.swapaxes(0, 1)
# %%
a.swapaxes(1, 0)
# %%
a = np.arange(1, 25).reshape(2, 3, 4)
a
# %%
np.swapaxes(a, 1, 2)
# %%
np.swapaxes(a, 1, 2).shape
# %%
"""
Differences:
np.swapaxes just swaps only two axes
but in np.transpose we can swap all the axes.
"""
