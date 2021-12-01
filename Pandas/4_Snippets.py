"""Look."""
# %%
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
"""Filtering the dataframe"""
filt = (df["last"] == "Doe")
# %%
"Call the data with the above filter."
df[filt]
# %%
"""This line does the same work that above line does."""
df.loc[filt]
# %%
df.loc[filt, "email"]

# %%
"""And Operator"""
filt = (df["last"] == "Doe") & (df["first"] == "John")

# %%
df.loc[filt, "email"]

# %%
"""Or Operator"""
filt = (df["last"] == "Schafer") | (df["first"] == "John")

# %%
df.loc[filt, "email"]

# %%
"""Not Operator(Supplement)"""
df.loc[-filt, "email"]

# %%
