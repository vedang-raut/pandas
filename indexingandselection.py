import pandas as pd
sales=pd.DataFrame({
    "Names":["Dmart","Croma","Reliance"],
    "Popularity":["High","Medium","Low"]
})
#Addition of the extra coumn that shows sales
sales['Places']=["Boisar","Umroli","Palghar"]
#In this line we have set the index to the Places
sales.set_index("Places",inplace=True)
#Here we have fetched the value using the index value
#print(sales.loc["Boisar","Names"])

sales.reset_index(inplace=True)

print(sales)