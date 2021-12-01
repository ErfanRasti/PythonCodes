# %%
"""Let's get familiar with changing the value of the rows and columns."""
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
"""It's better to always use inplace=True.
Because sometimes the pandas methods don't use it automatically."""
df.rename(columns={"ConvertedComp": "SalaryUSD"}, inplace=True)
# %%
df["SalaryUSD"]
# %%
df["Hobbyist"].map({"Yes": True, "No": False})
# %%
"""With map method every another values will convert to NaN value."""
df["Hobbyist"] = df["Hobbyist"].map({"Yes": True, "No": False})

# %%
df

# %%
