"""Look at this this snippet."""
# %%
import pandas as pd
# %%
person = {
    "first": "Corey",
    "last": "Schafer",
    "email": "CoreyMSchafer@gmail.com"
}

# %%

people = {
    "first": ["Corey"],
    "last": ["Schafer"],
    "email": ["CoreyMSchafer@gmail.com"]
}
# %%

people = {
    "first": ["Corey", 'Jane', 'John'],
    "last": ["Schafer", 'Doe', 'Doe'],
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com',
              'JohnDoe@email.com']
}

# %%
people["email"]
# %%
df = pd.DataFrame(people)
# %%
df
# %%
df["email"]
# %%
type(df["email"])
# Output: pandas.core.series.Series
"""email column is recognized as a series between first, last and email;
Also email itself is a series with three indexes."""
# %%
"""We can use df.email instead of df["email"]."""
df.email
"""It's better to use df["email"] form. One of the reasons is there are
some methods in pandas like df.count; It's possible that the name of column
gets conflict with methods like that."""
# %%
df.count
# %%
"""If we use one pair of brackets, pandas think we  wanna call one column
with this name: 'last', 'email'"""
df[['last', 'email']]
# %%
"""Show the list of columns."""
df.columns

# %%
"""Showing the rows..."""
"""With df.iloc we're searching by integer location."""
df.iloc[[0, 1]]

# %%
df.iloc[[0, 1], 2]

# %%
"""With df.loc we're seraching by label."""
df.loc[[0, 1]]
# %%
df.loc[[0, 1], "email"]

# %%
df.loc[[0, 1], ["email", "last"]]

# %%
