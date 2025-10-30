import pandas as pd
import numpy as np
companies=({
    "Names":["JP","EY","IBM","Goldman","Google"],
    "Locations":["Goregaon","Airoli","Pune","Banglore","Mumbai"],
    "Ranking":[1,2,3,4,5]
})
BIG4=pd.DataFrame(companies)
BIG4.set_index('Locations',inplace=True)

BIG4.reset_index(inplace=True)
#print(BIG4)


companies=pd.DataFrame({
    "Names":["JP","EY","IBM","Goldman","Google"],
    "Locations":["Goregaon","Airoli","Pune","Banglore","Mumbai"],
    "Ranking":[1,2,3,4,5]
}).set_index(["Names","Locations"])




#condition 
(BIG4[BIG4["Ranking"]<=4])

#query
(BIG4.query("Ranking>4"))

#sales=BIG4.to_csv("Companies.csv")
sales=pd.read_csv("Companies.csv")
#print(sales)

#Another way to create the dataframe

companies=({
    "Names":["JP","EY","IBM","Goldman","Google"],
    "Locations":"Mumbai",
    "Ranking":np.array([1,2,3,4,5])
})

data=pd.DataFrame(companies)
#print(data)





#this is about the handling of the missing data
School=pd.DataFrame({
    "Name":["Vedang","Hershey",None,"Swaraj","Vedang"],
    "Number":[2,3,None,5,2],
    "Marks":["Pass","Fail",None,"Pass","Pass"]
})

#print(School.dropna())
#print(School.drop_duplicates())
#print(School.replace("Vedang","raut"))
print(School["Name"].str.lower())