# %%
"""In this section we will learn how to sort data."""
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
df.sort_values(by=["Country", "ConvertedComp"],
               ascending=[True, False], inplace=True)
# %%
df[["Country", "ConvertedComp"]].head(50)
# %%
"""nlargest method shows us n largest values."""
df["ConvertedComp"].nlargest(10)
# %%
df.nlargest(10, "ConvertedComp")
# %%
"""nsmallest method shows us n smallest values."""
df["ConvertedComp"].nsmallest(10)
# %%
df.nsmallest(10, "ConvertedComp")
