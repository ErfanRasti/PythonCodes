# %%
"""We wanna get familiar with array manipulation(File 17-21)."""
import numpy as np
# %%
"""
np.insert won't change the original data.
It will return a copy of the data.
"""
help(np.insert)
# %%
a = np.arange(1, 11)
a
# %%
np.insert(a, 1, values=50)
# %%
np.insert(a, 10, values=50)
# %%
a
# %%
"""
It will convert the value to integer
then it will insert that to array.
"""
np.insert(a, 1, values=50.5)
# %%
np.insert(a, (1, 3), 50)
# %%
a = np.arange(1, 5).reshape(2, 2)
a
# %%
"""
It will take the default value that is none.
When axes is none, it will flatten the given array;  
Then it will insert the value."""
np.insert(a, 1, 23)
# %%
np.insert(a, 1, 23, axis=0)
# %%
np.insert(a, 1, 23, axis=1)
# %%
"""np.insert(a, 1, [1, 2, 3], axis=0) it will raise an error."""
np.insert(a, 1, [1, 2], axis=0)
# %%
np.insert(a, 1, (1, 2), axis=0)
# %%
"""
np.append won't change the original data.
It will return a copy of the data.
"""
help(np.append)
# %%
a = np.arange(1, 11)
a
# %%
np.append(a, 355)
# %%
a
# %%
a = np.arange(1, 5).reshape(2, 2)
a
# %%
np.append(a, [[4, 5]], axis=0)
# %%
np.append(a, [[4], [5]])
# %%
np.append(a, [[4], [5]], axis=1)
# %%
help(np.delete)
# %%
a = np.arange(1, 11)
a
# %%
"""
np.delete won't change the original data.
It will return a copy of the data.
"""
np.delete(a, 2)
# %%
a
# %%
a = np.arange(1, 5).reshape(2, 2)
# %%
np.delete(a, 2)
# %%
np.delete(a, 1, axis=0)
# %%
np.delete(a, 1, axis=1)
