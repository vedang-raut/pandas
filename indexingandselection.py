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
'''print(sales.loc["Boisar","Names"])'''
#Through this we have reset the index to default
sales.reset_index(inplace=True)

#here we have added the multiple indexes within the dataframe.
companies=pd.DataFrame({
    "Names":["IBM","EY","Goldmansachs","Infosys","Capgemini"],
    "Location":["USA","Germany","Europe","India","Uk"],
    "Profession":["Tech","Fin","Fin","Tech","Tech"],
    "Salary":[22,20,10,23,13]
}).set_index(["Location","Profession"])

#This is using the condition 
(companies[companies["Salary"]>=12])

print(companies.query('Salary>12'))