import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

file = pd.read_csv("co2_data.csv",header=5)


file["Average"]=file["Average"].replace(-99.99,math.nan)
file.dropna(subset=["Average"],inplace=True)

plt.scatter(file['decimal_year'],file["Average"])
b, a = np.polyfit(file["decimal_year"], file["Average"], deg=1)
plt.plot(file["decimal_year"], a + b * file["decimal_year"], color="k", lw=2.5)

plt.show()