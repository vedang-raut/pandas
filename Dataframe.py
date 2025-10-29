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
#print(sales.loc[1,'Profession'])  
#print(sales.iloc[0,1]) 




Powerlifters=pd.DataFrame({
    "Names":["Rupam","Manav","Swaraj","Hitanshu"],
    "Lifts":[260,200,200,250]
})



#ssf=Powerlifters[Powerlifters['Lifts']>250]
#print(ssf)


#

#print(Powerlifters)

#Powerlifters.loc[Powerlifters['Lifts']==260,250]=270

#Powerlifters.loc[Powerlifters['lifts']]
Powerlifters.rename(columns={"Names":"Giants"},inplace=True)



#djfc=Powerlifters.loc[Powerlifters["Giants"]=="Rupam","Giants"]="simpleshotz"

#ssf=Powerlifters.loc[Powerlifters["Lifts"]==260,"Lifts"]=280
#ssf=Powerlifters.rename(columns={"Giants":"ANGER"},inplace=True)


Powerlifters["GYM"]=["SSF","DJFC","EXplore","Tauras"]
#

#print(Powerlifters[Powerlifters["Lifts"]>200])




#print(Powerlifters[Powerlifters['Lifts']>200])
Powerlifters.rename(columns={"GYM":"Akada"},inplace=True)


Powerlifters.loc[Powerlifters["Akada"]=="SSF","Akada"]="sujit"

print(Powerlifters)