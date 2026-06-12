import pandas as pd
print("pandas")
df = pd.Series([10,20,30])
print(df)

dict = {"name":["dheeraj","sohan","mohan","praveen"],
        "age":[20,20,21,31],
        "salary":[100000,20000,3000,4000]}
df = pd.DataFrame(dict)
print(df)

# csv file access using the url
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file1.csv"
df = pd.read_csv(url)
print(df)

l = [10,20,30]
df = pd.Series(data=l)
print(df)

d = {
    "name":["sohan","shlok","pankaj","rishi","lalit"],
    "age":[20,21,22,22,22],
    "roll_no":[110,111,112,113,114]
}
# df = pd.Series(data= d)
df = pd.DataFrame(data = d)
print(df)

url = "https://raw.githubusercontent.com/sohan765/DS-45-days/main/file2%20-%20Sheet1.csv"
df = pd.read_csv(url)
# print(df)

data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
    "Experience": [2, 3, 5, 4, 1, 3]
}

df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.head(2))
print(df.tail())
print(df.tail(4))
print(df.tail(-2))
print(df.info())
print(df.describe())

df.rename(columns={"Name": "Emp_Name"}, inplace=True)
print(df)

print(df.shape)