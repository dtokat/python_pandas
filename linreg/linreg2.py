import matplotlib.pyplot as plt
from scipy import stats

x = [1,2,3,4,5]
y = [2,4,5,4,5]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

# plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
print(slope)
print(intercept)
print(r)
print("lololo")