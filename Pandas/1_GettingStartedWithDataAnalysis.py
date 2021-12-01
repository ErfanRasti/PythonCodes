"""Let's get familiar with Pandas Library; A library for datascientists."""
# %%
import pandas as pd
# %%
"""Read the dataframe."""
df = pd.read_csv("developer_survey_2019/survey_results_public.csv")
# %%
df

# %%
"""Print the number of rows and column."""
df.shape

# %%
"""Show some information about our dataframe."""
df.info()
# %%
"""Set the maximum number of the columns to 85."""
pd.set_option("display.max_columns", 85)
"""Set the maximum number of the rows to 85."""
pd.set_option("display.max_rows", 85)

# %%
"""Schema form shows us what's the definition of each column."""
schema_df = pd.read_csv("developer_survey_2019/survey_results_schema.csv")

# %%
schema_df
# %%
"""DataFrame.head(n=5) shows us first n rows."""
df.head()
# %%
"""DataFrame.tail(n=5) shows us last n rows."""
df.tail(10)
# %%
