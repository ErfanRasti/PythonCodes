# %%
"""Let's get familiar with working with time series."""
import pandas as pd
df = pd.read_csv("Dataframes/ETH_1h.csv")
# %%
df.head()
# %%
df.shape
# %%
"""Show us the last date."""
df.loc[0, "Date"]
# %%
"""
df.loc[0, "Date"].day_name()

It will raise an error.
AttributeError: 'str' object has no attribute 'day_name'


df["Date"] = pd.to_datetime(df["Date"])

It will raise an error.
ParserError: Unknown string format: 2020-03-13 08-PM

datetime formats:
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

We should convert the dataframe form to pandas standard form.
"""
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d %I-%p")
# %%
df["Date"]
# %%
df.loc[0, "Date"]
# %%
df.loc[0, "Date"].day_name()
# %%
"""
date, datetime, and time objects all support a strftime(format) method,
to create a string representing the time under the control of an explicit
format string.
Conversely, the datetime.strptime() class method creates a datetime object
from a string representing a date and time and a corresponding format string.

pd.datetime.strptime:
string, format -> new datetime parsed from a string (like time.strptime()).

If we wanna to convert this to a date as we are loading our data,
then we can also do that as below:
"""


def d_parser(x):
    """Define dataframe time format for pandas."""
    return pd.datetime.strptime(x, "%Y-%m-%d %I-%p")

# We can use lambda function instead.
# d_parser= lambda x: pd.datetime.strptime(x,"%Y-%m-%d %I-%p")


df = pd.read_csv("Dataframes/ETH_1h.csv",
                 parse_dates=["Date"], date_parser=d_parser)
# %%
df.head()
# %%
df["Date"]
# %%
df["Date"].dt.day_name()
# %%
df["DayOfWeek"] = df["Date"].dt.day_name()
# %%
df
# %%
df["Date"].min()
# %%
df["Date"].max()
# %%
"""Calculate the number of under-check days."""
df["Date"].max()-df["Date"].min()
# %%
filt = (df["Date"] >= "2019")
df.loc[filt]
# %%
filt = (df["Date"] >= "2019") & (df["Date"] < "2020")
df.loc[filt]
# %%
filt = (df["Date"] >= "2019-01-01") & (df["Date"] < "2020-01-01")

# We can use actual datetime as below:
# filt = (df["Date"] >= pd.to_datetime("2019-01-01")
#         ) & (df["Date"] < pd.to_datetime("2020-01-01"))

df.loc[filt]
# %%
df.set_index("Date", inplace=True)
# %%
df["2019"]
# %%
df["2020-01":"2020-02"]
# %%
df["2020-01":"2020-02"]["Close"]
# %%
df["2020-01":"2020-02"]["Close"].mean()
# %%
df["2020-01":"2020-02"].head(24)
# %%
df["2020-01-01"]["High"]
# %%
df["2020-01-01"]["Close"]
# %%
df["2020-01-01"]["High"].max()
# %%
"""
Set maximum of high values according to the day attribute.

https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects
"""
df["High"].resample("D").max()
# %%
"""Set maximum of high values according to the week attribute."""
df["High"].resample("W").max()
# %%
"""Set maximum of high values according to the day attribute."""
df["High"].resample("D")
highs = df["High"].resample("D").max()
# %%
highs["2020-01-01"]
# %%
"""
%matplotlib notebook: will lead to interactive plots embedded within
the notebook, you can zoom and resize the figure

%matplotlib inline: only draw static images in the notebook
"""
# %matplotlib inline
# %%
highs.plot()
# %%
"""Show the mean values for each of the columns on a weekly basis."""
df.resample("W").mean()
# %%
df.resample("W").agg(
    {"Close": "mean", "High": "max", "Low": "min", "Volume": "sum"})
