import pandas as pd
sales=pd.Series([2,4,3,1,9,5])

#The attributes
print(sales.values)
print(sales.index)
print(sales.dtype)


#the methods
print(sales.count())
print(sales.head(2))
print(sales.tail(2))
print(sales.isnull())
print(sales.sort_values())



sales2=pd.Series(data=[1,2,3,4], index=list("abcd"))
print(sales2)