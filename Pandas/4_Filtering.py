"""In this code we're gonna be learning more about indexes."""
# %%
import pandas as pd

# %%
"""Set the Respondent column as indexes."""
df = pd.read_csv(
    "developer_survey_2019/survey_results_public.csv", index_col="Respondent")

"""Set the Column column as indexes."""
schema_df = pd.read_csv(
    "developer_survey_2019/survey_results_schema.csv", index_col="Column")
# %%
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)
# %%
df.head()
# %%
"""df["ConvertedComp"] > 70000 makes a list of True and False.
If the number is more than 70000 it returns True and vice versa."""
high_salary = (df["ConvertedComp"] > 70000)
high_salary

# %%
df.loc[high_salary]
# %%
df.loc[high_salary, ["Country", "LanguageWorkedWith", "ConvertedComp"]]

# %%
countries = ["United States", "India", "United Kingdom", "Germany", "Canada"]
filt = df["Country"].isin(countries)
filt

# %%
df.loc[filt, "Country"]
# %%
df["LanguageWorkedWith"]
# %%
"""na= is because we have some NaN data. If we don't use it,
it will raise an error.
na=False means we're not gonna do anything with NaN data
and filter doesn't contain these data.
na=True means filter contains these data."""
filt = df["LanguageWorkedWith"].str.contains("Python", na=False)

# %%
df.loc[filt, "LanguageWorkedWith"]
# %%
filt

# %%
