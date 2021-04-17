from bs4 import  BeautifulSoup
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


df = pd.read_csv('movies_dataframe.csv')

#print(df.head())

group = df.groupby('Year').Rating.mean().reset_index()

#print(group.head())


ax = plt.subplot()
rating=list(group['Rating'])
year = list(group['Year'])

# print(np.std(rating))
# print(np.mean(rating))


plt.plot(year,rating)
plt.xlabel('year')
plt.ylabel('rating')
#print(year)
# ax.set_xticks(year)
# ax.set_xticklabels(year)
b = 0.1
ax.axis([year[0]-b,year[-1]+b,6,8])
plt.plot(np.unique(year), np.poly1d(np.polyfit(year, rating, 1))(np.unique(year)))

#plt.hist(rating)
plt.show()


