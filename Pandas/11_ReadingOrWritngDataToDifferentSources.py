# %%
"""
Converting dataframes to another formats is very important.

In this section we wanna get familiar with reading/writing data to
different sources(Excel, JSON, SQL, Etc.).
"""
import pandas as pd
import os
import psycopg2
from sqlalchemy import create_engine
# %%
df = pd.read_csv(
    "developer_survey_2019/survey_results_public.csv", index_col="Respondent")
schema_df = pd.read_csv(
    "developer_survey_2019/survey_results_schema.csv", index_col="Column")
# %%
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
# %%
df.head()
# %%
filt = (df["Country"] == "India")
india_df = df.loc[filt]
india_df.head()
# %%
"""
Save dataframe as .csv file.
(If there is file with exact name, It will replace it.)
"""
india_df.to_csv("Dataframes/modified.csv")
# %%
"""Save dataframe as .tsv file and separate words by tab."""
india_df.to_csv("Dataframes/modified.tsv", sep='\t')
# %%
"""Save dataframe as .xlsx file."""
india_df.to_excel("Dataframes/modified.xlsx")
# %%
"""Read modifie.xlsx."""
test = pd.read_excel("Dataframes/modified.xlsx", index_col="Respondent")
# %%
test
# %%
"""Save dataframe as .json file."""
india_df.to_json("Dataframes/modified.json")
# %%
"""Save dataframe as modified.json and orient it by records and put
each one in new line."""
india_df.to_json("Dataframes/modified.json", orient="records", lines=True)
# %%
"""Read modified.json."""
test = pd.read_json("Dataframes/modified.json", orient="records", lines=True)
# %%
test.head()
# %%
"""
Creating an engine and connecting to a database
user and password of the database are in user environment variables.
"""
engine = create_engine("postgresql://{0}:{1}@localhost:5432/sample_db".format(
    os.environ.get("DB_USER"), os.environ.get("DB_PASS")))
# %%
"""
Creating a new table on the database
If sample_table exists, replace it.
"""
india_df.to_sql("sample_table", engine, if_exists='replace')
# %%
"""Reading the dataframe from an sql database"""
sql_df = pd.read_sql("sample_table", engine, index_col="Respondent")
# %%
sql_df.head()
# %%
"""Running a specific sql query in order to load in our data"""
sql_df = pd.read_sql_query(
    "SELECT * FROM sample_table", engine, index_col="Respondent")
# %%
sql_df.head()
# %%
"""Importing data from a URL"""
posts_df = pd.read_json("https://raw.githubusercontent.com/"
                        "CoreyMSchafer/code_snippets/master/"
                        "Python/Flask_Blog/snippets/posts.json")
# %%
posts_df.head()
# %%
