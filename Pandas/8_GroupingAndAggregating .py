# %%
"""
Let's get familiar with Grouping and Aggregating.

Aggregating means combining multiple pieces of data into a single result.
Mean, median or the mod are aggregating functions.
"""
import pandas as pd
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
"""In this column NaN means they ignore this question
and don't answer to that."""
df["ConvertedComp"].head(15)
# %%
df["ConvertedComp"].median()
# %%
df.median()
# %%
"""df.describe() gives us count, mean, std, min, max and
some quantiles(25%, 50%, 75%)."""
df.describe()
# %%
df["ConvertedComp"].count()
# %%
df["Hobbyist"]
# %%
df["Hobbyist"].value_counts()
# %%
df["SocialMedia"]
# %%
schema_df.loc["SocialMedia"]
# %%
df["SocialMedia"].value_counts()
# %%
"""Percentage form"""
df["SocialMedia"].value_counts(normalize=True)
# %%
"""
grouping our data:
A group by operation involves some combination of splitting up
our object applying a function and then combining those results
1_Splitting
2_Apply function
3_Combining the results
"""
df["Country"]
# %%
df["Country"].value_counts()
# %%
df.groupby(["Country"])
# %%
country_grp = df.groupby(["Country"])
# %%
country_grp.get_group("United States")
# %%
"""Finding the most popular socialmedia in each country"""
filt = df["Country"] == "United States"
df.loc[filt]["SocialMedia"].value_counts()
# %%
country_grp["SocialMedia"].value_counts()
# %%
country_grp["SocialMedia"].value_counts().head(50)
# %%
"""country_grp method is better than filt way to doing this.
Because we don't need reload filter over and over."""
country_grp["SocialMedia"].value_counts().loc["United States"]
# %%
country_grp["ConvertedComp"].median()
# %%
country_grp["ConvertedComp"].median().loc["Germany"]
# %%
"""agg: Aggregating Methods"""
country_grp["ConvertedComp"].agg(["median", "mean"])
# %%
country_grp["ConvertedComp"].agg(["median", "mean"]).loc["Canada"]
# %%
filt = (df["Country"] == "India")
df.loc[filt]["LanguageWorkedWith"]
# %%
df.loc[filt]["LanguageWorkedWith"].str.contains("Python")
# %%
"""
True : 1
False : 0
"""
df.loc[filt]["LanguageWorkedWith"].str.contains("Python").sum()
# %%
"""
It will raise an error.

country_grp["LanguageWorkedWith"].str.contains("Python").sum()

AttributeError: 'SeriesGroupBy' object has no attribute 'str'
"""
country_grp["LanguageWorkedWith"].apply(
    lambda x: x.str.contains("Python").sum())
# %%
country_respondents = df["Country"].value_counts()
country_respondents
# %%
country_uses_python = country_grp["LanguageWorkedWith"].apply(
    lambda x: x.str.contains("Python").sum())
country_uses_python
# %%
"""Concatenate two columns to make a new dataframe."""
python_df = pd.concat(
    [country_respondents, country_uses_python], axis="columns", sort=False)
python_df
# %%
python_df.rename(columns={"Country": "NumRespondants",
                          "LanguageWorkedWith": "NumKnowsPython"},
                 inplace=True)
# %%
python_df
# %%
python_df["PctKnowsPython"] = (
    python_df["NumKnowsPython"]/python_df["NumRespondants"]*100)

# %%
python_df
# %%
python_df.sort_values(by="PctKnowsPython", ascending=False, inplace=True)
# %%
python_df
# %%
python_df.head(50)
# %%
python_df.loc["Japan"]
# %%
python_df.sort_values(
    by=["NumRespondants", "PctKnowsPython"], ascending=False, inplace=True)
# %%
python_df.head(50)

# %%
