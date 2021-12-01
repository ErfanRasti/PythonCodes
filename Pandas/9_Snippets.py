# %%
"""..."""
import pandas as pd
import numpy as np
# %%
people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'],
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com',
              'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}
# %%
df = pd.DataFrame(people)

df.replace("NA", np.nan, inplace=True)
df.replace("Missing", np.nan, inplace=True)
# %%
df
# %%
"""Drop NaN data."""
df.dropna()
# %%
"""
axis : {0 or 'index', 1 or 'columns'}, default 0 Determine
if rows or columns which contain missing values are removed.

* 0, or 'index' : Drop rows which contain missing values.
* 1, or 'columns' : Drop columns which contain missing value.


how : {'any', 'all'}, default 'any' Determine if row or column
is removed from DataFrame, when we have at least one NA or all NA.

* 'any' : If any NA values are present, drop that row or column.
* 'all' : If all values are NA, drop that row or column.
"""
df.dropna(axis="index", how="all", subset=["email"])
# %%
df.dropna(axis="index", how="all", subset=["last", "email"])
# %%
df.isna()
# %%
df.fillna("MISSING")
# %%
df.fillna(0)
# %%
"""
looking for data types...
df.dtypes is not a method, it's an attribute.

object means string or mix of different things.
"""
df.dtypes
# %%
"""
df["age"].mean()

It will raise an error.
TypeError: can only concatenate str (not "int") to str

If we use dropna, it will work.
str with str, int with int!
"""
df["age"]
# %%
"""NaN is a float; So we can't concatenate it with an string."""
type(np.nan)
# %%
"""
df["age"]=df["age"].astype(int)

It will raise an error. NaN is a float.
It Can't be converted to an integer.

TypeError: int() argument must be a string, a bytes-like object
or a number, not 'NoneType'
"""
df["age"] = df["age"].astype(float)
df["age"]
# %%
df.dtypes
# %%
df["age"].mean()

# %%
