# %%
"""You know what to do."""
import pandas as pd

# %%
people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com",
              "JaneDoe@email.com",
              "JohnDoe@email.com"]
}

# %%
df = pd.DataFrame(people)
# %%
df
# %%
df["first"] + " " + df["last"]
# %%
"""Add full_name column."""
df["full_name"] = df["first"] + " " + df["last"]
# %%
df
# %%
"""Remove first and last columns."""
df.drop(columns=["first", "last"], inplace=True)
# %%
df
# %%
df["full_name"].str.split(" ", expand=True)
# %%
df[["first", "last"]] = df["full_name"].str.split(" ", expand=True)
# %%
df
# %%
"""Adding a new row"""
"""If we don't use ignore_index=True, it will raise an error."""
df.append({"first": "Tony"}, ignore_index=True)

# %%
people = {
    'first': ['Tony', 'Steve'],
    'last': ['Stark', 'Rogers'],
    'email': ['IronMan@avenge.com', 'Cap@avenge.com']
}
df2 = pd.DataFrame(people)
# %%
df2
# %%
"""Adding a dataframe to another one."""
"""If we wanna assign indexes properly, we should use ignore_index=True."""
"""We use sort=False to prevent raising a warning."""
df.append(df2, ignore_index=True, sort=False)
# %%
df = df.append(df2, ignore_index=True, sort=False)
# %%
df
# %%
df.drop(index=4, inplace=True)
# %%
df
# %%
"""Dropping a row"""
filt = (df["last"] == "Doe")
df.drop(index=df[filt].index)
