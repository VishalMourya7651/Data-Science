import pandas as pd

url = "https://www.basketball-reference.com/leagues/NBA_2015_totals.html"

dfs = pd.read_html(url)   # returns a list of DataFrames
df = dfs[0]               # get the first (main) table

print(df.head())
