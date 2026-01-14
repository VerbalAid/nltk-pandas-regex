import pandas as pd

df = pd.read_csv("Euro2012.csv", encoding="utf-8")

euro12 = df.loc[:, ~df.columns.str.contains('^Unnamed')]

print("\nFirst 5 entries:")
print(euro12.head()) # First 5 entries 

print(f"Number of Teams: {euro12['Team'].nunique()}") # Lists all of the Teams = 15

print("\nNumber of columns:")
print(euro12.shape[1]) # Shows the number of colunms 

print("\nNames of the Columns:")
print(euro12.columns.tolist())  #lists all of the columns

print("\n 10th Column name")
print(euro12.columns[9])