import pandas as pd
import numpy as np
data = {
    "name" :["Sohan","Shlok","Pankaj","Rishi"],
    "City" :["Jodhpur","Tonk","Bondi","Alwar"],
    "Age" : [19,19,21,20],
    "Salary" : [200000,30000,15000,102233]
}
df = pd.DataFrame(data)
print(df)
print(df["name"])

df["destination"] = ["paris","mumbai","kolkata","USA"]
# print(df)
print(df.drop("destination",axis= 1))
print(df.drop(2,axis=0))

print(df.loc[[0,1]])
print(df.iloc[3])

print(df.loc[[0,1]][["Age","Salary"]])

data1 = {
    "A" :[1,2,np.nan,4,5],
    "B" : [1,2,3,4,5],
    "C" : [1,2,3,np.nan,np.nan],
    "D" : [np.nan,2,np.nan,np.nan,5]
}
df1 = pd.DataFrame(data1)
print(df1)
print(df1.isna())
print(df1.isna().sum())
print(df1.isna().any())
it is work on the rows
print(df1.dropna())
print(df1.dropna(thresh=3))

# fillna is work on the bases of column
print(df1.fillna(0))
values = {"A":10,"B":20,"C":30,"D":40}
print(df1.fillna(value=values,inplace = True))
print(df1)
print(df1["A"].mean())

print(df1['A'].agg(['mean','max','min','sum']))
