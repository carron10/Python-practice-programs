from pandas import read_excel
from matplotlib import pyplot
series = read_excel(r'C:\Users\Muleya\Desktop\PYTHON PROJECTS\MONTHLY SALES DATA1.xlsx', header=0, index_col=0)
series.plot()
pyplot.show()