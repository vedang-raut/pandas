import pandas as pd

School=pd.DataFrame({
    "Name":["Vedang","Hershey",None,"Swaraj","Vedang"],
    "Number":[2,3,4,5,2],
    "Marks":["Pass","Fail","Pass","Pass","Pass"]
})

#print(School.dropna())
#print(School.fillna(0))

#print(School.drop_duplicates())

#print(School.replace("Vedang","Raut"))
School['Number']=School['Number'].astype(float)

School['Marks']=School['Marks'].str.lower()
print(School)