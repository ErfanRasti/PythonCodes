# %%
"""Look again."""
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
df.columns

# %%
"""Rename the columns."""
df.columns = ["first name", "last name", "email"]

# %%
df.columns
# %%
df
# %%
"""Make all of the columns' title, upper-case."""
df.columns = [x.upper() for x in df.columns]

# %%
df
# %%
"""Replace spaces with underscores."""
df.columns = df.columns.str.replace(" ", "_")

# %%
df
# %%
"""Make all of the columns' title, lower-case."""
df.columns = [x.lower() for x in df.columns]
# %%
df
# %%
"""inplace=True renames the columns of main df dataframe."""
df.rename(columns={"first_name": "first", "last_name": "last"}, inplace=True)

# %%
df
# %%
df.loc[2]
# %%
df.loc[2] = ["Erfan", "Rasti", "erfanrasty@gmail.com"]

# %%
df
# %%
df.loc[2, ["first", "last", "email"]] = ["John", "Doe", "JohnDoe@email.com"]

# %%
df
# %%
df.loc[2, "last"] = "Smith"

# %%
df
# %%
"""df.at is like df.loc when we wanna get or set a single value;
But the performance of df.at is more."""
df.at[2, "last"] = "Doe"

# %%
df
# %%
filt = (df["email"] == "JohnDoe@email.com")
df[filt]
# %%
"""We can't use df[filt]["last"]='Smith' to change the value.
It will raise a Warning and it won't change the value."""
df[filt]["last"]
df[filt]["last"] = "Smith"
# %%
df
# %%
df[filt]["last"]
df.loc[filt, "last"] = "Smith"

# %%
df
# %%
"""Make all email addresses lower-case."""
df["email"].str.lower()
# %%
"""Change the main dataframe email addresses to lower-case."""
df["email"] = df["email"].str.lower()
# %%
df
# %%
"""Four similar methods: 1_apply 2_applymap 3_map 4_replace
1_Let's get familiar with apply method."""
df["email"].apply(len)
# %%


def update_email(email):
    """Make email addresses, upper-case."""
    return email.upper()


# %%
"""We should use functions without parentheses in apply method."""
df["email"].apply(update_email)
# %%
df["email"] = df["email"].apply(update_email)

# %%
df
# %%
"""Using lambda function"""
df["email"] = df["email"].apply(lambda x: x.lower())

# %%
df
# %%
df["email"].apply(len)
# %%
"""df.apply(len) gives us the number of members of every column."""
df.apply(len)
# %%
len(df["email"])
# %%
df.apply(len, axis="columns")
# %%
"""pd.Series.min method shows the minimum of alphabetical sort."""
df.apply(pd.Series.min)
# %%
df.apply(lambda x: x.min())
# %%
"""2_applymap"""
"""df.applymap(len) calculates the length of each argument."""
df.applymap(len)
# %%
df.applymap(str.lower)
# %%
"""3_map"""
"""If we don't assign a value to an argument, it will get NaN."""
df["first"].map({"Corey": "Chris", "Jane": "Mary"})

# %%
df
# %%
"""4_replace"""
"""If we don't assign value to an argument, it will call the last value."""
df["first"].replace({"Corey": "Chris", "Jane": "Mary"})
# %%
df
# %%
df["first"] = df["first"].replace({"Corey": "Chris", "Jane": "Mary"})

# %%
df

# %%
