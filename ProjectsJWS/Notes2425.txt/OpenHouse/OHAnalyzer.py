import pandas as pd



df = pd.read_csv("RandomData/Foyer.csv",header=0)
print(df)

schools = df["school"].unique()
print(schools)


