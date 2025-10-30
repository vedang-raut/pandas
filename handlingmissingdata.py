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
#print(School)





Gym=pd.DataFrame({
    "Names":["Rupam","Manav","Aakash"],
    "Exercise":["Deadlift","Overall","Overall"],
    "Highest":[260,200,150]
})

#print(Gym.set_index("Exercise",inplace=True))

#print(Gym.reset_index(inplace=True))

#print(Gym.query("Highest>=200"))
#print(Gym[Gym["Highest"]>150])

#data=Gym.to_csv("lifters.csv")
data=pd.read_csv("lifters.csv")
print(data)