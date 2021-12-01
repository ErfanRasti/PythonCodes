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
df.loc[1]
# %%
schema_df
# %%
schema_df.loc["Hobbyist"]
# %%
schema_df.loc["MgrIdiot"]

# %%
schema_df.loc["MgrIdiot", "QuestionText"]

# %%
schema_df
# %%
schema_df.sort_index()
# %%
schema_df.sort_index(ascending=False)


# %%
schema_df.sort_index(ascending=True)
