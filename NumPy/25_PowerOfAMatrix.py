# %%
"""
It is obvious.

Isn't?
"""
import numpy as np
# %%
help(np.linalg.matrix_power)
# %%
a = np.arange(1, 5).reshape((2, 2))
a
# %%
np.linalg.matrix_power(a, 2)
# %%
a.dot(a)
# %%
a**a
# %%
np.linalg.matrix_power(a, 0)

# %%
np.linalg.matrix_power(a, -1)

# %%
np.linalg.matrix_power(a, -2)
# %%
b = np.linalg.inv(a)
# %%
np.linalg.matrix_power(b, 2)
# %%
"""
np.linalg.matrix_power(a,1.5)
will raise an error.(Power should be integer.)"""
