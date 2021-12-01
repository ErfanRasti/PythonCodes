# %%
"""Look forever."""
import pandas as pd
# %%
people = {
    "first": ["Corey", "Jane", "John", "Adam"],
    "last": ["Schafer", "Doe", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com",
              "JohnDoe@email.com", "A@email.com"]
}

# %%
df = pd.DataFrame(people)
# %%
df
# %%
"""Sort data by last column."""
df.sort_values(by="last", ascending=False)
# %%
df
# %%
"""If we pass a list of column names to the by= ,
if the first sort mask was equal, the second will be used."""
df.sort_values(by=["last", "first"], ascending=False)
# %%
df.sort_values(by=["last", "first"], ascending=[False, True], inplace=True)

# %%
df
# %%
df.sort_index()
df
# %%
df["last"].sort_values()
# %%
