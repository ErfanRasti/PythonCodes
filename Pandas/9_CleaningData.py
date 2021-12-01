# %%
"""Cleaning data is so important; Look carefully."""
import pandas as pd
# %%
na_vals = ["NA", "Missing"]
df = pd.read_csv("developer_survey_2019/survey_results_public.csv",
                 index_col="Respondent", na_values=na_vals)
schema_df = pd.read_csv(
    "developer_survey_2019/survey_results_schema.csv", index_col="Column")
# %%
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
# %%
df.head()
# %%
df["YearsCode"].head(10)
# %%
"""
df["YearsCode"].mean()

It will raise an error.
TypeError: can only concatenate str (not "int") to str


df["YearsCode"]=df["YearsCode"].astype(float)

It will raise an error again.

ValueError: could not convert string to float: 'Less than 1 year'
"""
df["YearsCode"].unique()
# %%
df["YearsCode"].replace("Less than 1 year", 0, inplace=True)
df["YearsCode"].replace("More than 50 years", 51, inplace=True)
# %%
df["YearsCode"].unique()
# %%
df["YearsCode"] = df["YearsCode"].astype(float)
# %%
df["YearsCode"].mean()
# %%
df["YearsCode"].median()
