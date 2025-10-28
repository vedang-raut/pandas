import pandas as pd
sales= pd.DataFrame({
    'Name': ["vedang","Swaraj"],
    'Profession': ["Engineer","Architect"]
})

#print(sales)


#The dataseries can be also converted into dataframe

sales1=pd.Series(["Vedang","Swaraj","Neha"])
sales2=pd.Series(["Engineer","Architecture","Doctor"])

majorsales=pd.DataFrame({'c1':sales1,
                         'c2': sales2})
#print(majorsales)


#print(majorsales.dtypes)
#print(majorsales.shape)

#let us access the the data with coumn name
print(sales.loc[1,'Profession'])  
print(sales.iloc[0,1]) 
