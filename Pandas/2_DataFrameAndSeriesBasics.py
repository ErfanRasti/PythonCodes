"""Let's get familiar with dataframe and series."""
# %%
import pandas as pd
# %%
df = pd.read_csv("developer_survey_2019/survey_results_public.csv")
schema_df = pd.read_csv("developer_survey_2019/survey_results_schema.csv")

# %%
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)

# %%
df.head()
# %%
schema_df
# %%
df.shape
# %%
"""df.columns shows us the list of columns' names."""
df.columns
# %%
df["Hobbyist"]
# %%
df["Hobbyist"].value_counts()
# %%
df.loc[0]
# %%
df.loc[[0, 1, 2], "Hobbyist"]
# %%
"""Show us first 3 rows.(0, 1, 2)"""
df.loc[0:2, "Hobbyist"]
# %%
"""Inclusive Form"""
df.loc[0: 2, "Hobbyist": "Employment"]

# %%
