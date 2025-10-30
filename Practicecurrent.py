import pandas as pd
GYM=pd.DataFrame({
    "Names":["Rupam","Manav","Swaraj","Hitanshu"],
    "Lifts":[260,200,210,260]
})

ssf=GYM[GYM["Lifts"]>200]
#print(ssf)


GYM["Location"]=["Palghar","Palghar","Palghar","Palghar"]

#ssf=Powerlifters.rename(columns={"Giants":"ANGER"},inplace=True)
GYM.rename(columns={"Location":"place"},inplace=True)


GYM.loc[GYM['place']=="Palghar","place"]="umroli"





GYM.rename(columns={"place":"Locationarea"},inplace=True)

GYM.loc[GYM["Names"]=="Rupam","Names"]="simpleshotz"
print(GYM) 



