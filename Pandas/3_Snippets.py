"""Just look."""
# %%
import pandas as pd

# %%
people = {
    "first": ["Corey", 'Jane', 'John'],
    "last": ["Schafer", 'Doe', 'Doe'],
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com',
              'JohnDoe@email.com']
}

# %%
df = pd.DataFrame(people)
# %%
df
# %%
df["email"]
# %%
"""Set the email address as the index for the dataframe.
It doesn't modify the main dataframe(df)."""
df.set_index("email")
# %%
df
# %%
"""inplace=True replaces the indexes with new set index."""
df.set_index("email", inplace=True)

# %%
df
# %%
df.index
# %%
df.loc["CoreyMSchafer@gmail.com"]
# %%
"""df.loc[0] will raise an error. If we wanna call
arguments via integer we should use df.iloc[]"""
df.loc["CoreyMSchafer@gmail.com", "last"]

# %%
"""Reset the index form to default."""
df.reset_index(inplace=True)
df

# %%
