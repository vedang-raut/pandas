import pandas as pd
pd.__version__
#sales = pd.Series([2,None,4,5])  #This is used to create the series of data which can inside the list or tuple
#print(sales)

#print(sales[0]) This is called indexing in which the a particular index data is fetched.

#print(sales[0:4]) This is called slicing where the particular slice is get means the combination

'''
print(sales.dtype)
print(sales.index)
print(sales.values)'''

#methods
#print(sales.tail(1))

#print(sales.head(1))

# print(sales.count())

#sales1=pd.Series([1,4,5,7,2,3,6])
'''print(sales1.count())
print(sales1.index)
print(sales1.values)
print(sales1.dtype)'''
#print(sales1.head())

#print(sales1.sort_values())

#print(sales1.isnull())

#sales*2
#print(sales*2)

#print(sales.isnull())

#print(sales.fillna(0))



sales3=pd.Series(data=[2,2,3,4,5],index=list('abcde'))
print(sales3)



print(sales3.fillna(0))
