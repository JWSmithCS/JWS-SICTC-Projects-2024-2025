import pandas as pd


df = pd.read_csv('highscores.csv',header=0)
print(df["First_name"])

hscorer=df.loc[df['integer']==1000,"first_name"]
hscorer=df.loc[df['integer']==1000,"first_name"].iloc[0]
print(hscorer)
sortDF = df.sort_values(by="integer")
sortDF.to_csv('highscores-sorted.csv',index=False)