# About this file
# Food servers’ tips in restaurants may be influenced by many
# factors, including the nature of the restaurant, size of the party, and table
# locations in the restaurant. Restaurant managers need to know which factors
# matter when they assign tables to food servers. For the sake of staff morale,
# they usually want to avoid either the substance or the appearance of unfair
# treatment of the servers, for whom tips (at least in restaurants in the United
# States) are a major component of pay.
# In one restaurant, a food server recorded the following data on all cus-
# tomers they served during an interval of two and a half months in early 1990.
# The restaurant, located in a suburban shopping mall, was part of a national
# chain and served a varied menu. In observance of local law, the restaurant
# offered to seat in a non-smoking section to patrons who requested it. Each
# record includes a day and time, and taken together, they show the server’s
# work schedule.

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

df = pd.read_csv('tips.csv')
print(df.head(4))  #To see first 4 rows

y = df['tip']
x1= df['total_bill']
slope, intercept, r, p, std_err = stats.linregress(x1, y)

def myfunc(x):
  return slope * x + intercept
mymodel = list(map(myfunc, x1))
plt.plot(x1, mymodel)

plt.scatter(x1,y)
plt.xlabel('Total Bill', fontsize = 12)
plt.ylabel('Tip', fontsize = 12)
plt.show()
print(slope)
print(intercept)

# ŷ= 0,9203+0,105x
print(r)
# r=0.675    shows that there is a relationship, not perfect, but it indicates that we could use linear regression in future predictions.

# R for Relationship
# It is important to know how the relationship between the values of the x-axis and the values of the y-axis is, if there are no relationship the linear regression can not be used to predict anything.
# This relationship - the coefficient of correlation - is called r.
# The r value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.
# Python and the Scipy module will compute this value for you, all you have to do is feed it with the x and y values.

