from pandas import read_excel
from matplotlib import pyplot
series = read_excel(r'C:\Users\Muleya\Desktop\PYTHON PROJECTS\MONTHLY SALES DATA1.xlsx', header=0, index_col=0)
series.hist()
pyplot.show()

X = series.values
split = round(len(X) / 2)
X1, X2 = X[0:split], X[split:]
mean1, mean2 = X1.mean(), X2.mean()
var1, var2 = X1.var(), X2.var()
print('mean1=%f, mean2=%f' % (mean1, mean2))
print('variance1=%f, variance2=%f' % (var1, var2))