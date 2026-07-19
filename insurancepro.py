import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv(r"insurance.csv")
# print(df)

#  EDA
# print(df.shape)
# print(df.head())
# print(df.info())
# print(df.describe())

# print(df.isna().sum())
# print(df.columns)

numeric_columns = ['age',  'bmi', 'children',  'charges']
# for col in numeric_columns:
#     plt.figure(figsize = (6,4))
#     print(sns.histplot(df[col],kde = True,bins = 20 )) # kde kuneral density curve ke liye kde = True kiya hai
#     plt.xlabel(col)
#     plt.ylabel("Frequency")
#     plt.show()

# sns.countplot(x = df['children'])
# plt.xlabel('children')
# plt.ylabel('count')
# plt.show() 
# sns.countplot(x = df['sex'])
# plt.xlabel('sex')
# plt.ylabel('count')
# plt.show()

# sns.countplot(x = df['smoker'])
# plt.xlabel('smoker')
# plt.ylabel('count')
# plt.show()

# for col in numeric_columns:
#     plt.figure(figsize=(6,4))
#     sns.boxplot(x = df[col])
#     plt.xlabel(col)
#     plt.ylabel('count')
#     plt.show()

# plt.figure(figsize= (8,6))
# sns.heatmap(df.corr(numeric_only=True),annot = True,cmap = "coolwarm",fmt=".2f")

# plt.show()

# data Cleaning and preprocessing
df_cleaned = df.copy()
# print(df_cleaned.head())
# print(df_cleaned.drop_duplicates(inplace = True))  # for remove duplicate
# print(df_cleaned.isnull.sum())

# print(df_cleaned.dtypes)
df_cleaned['sex'].value_counts()
df_cleaned['sex'] = df_cleaned['sex'].map({"male":0,"female":1})
# print(df_cleaned)

df_cleaned['smoker'] = df_cleaned['smoker'].map({"yes":1,"no":0})
# print(df_cleaned)
df_cleaned.rename(columns={
    "sex":"is_female",
    "smoker":"is_smoker"},inplace = True)
# print(df_cleaned.head())


df['region'].value_counts()
# one hot coding apply into the region
df_cleaned = pd.get_dummies(df_cleaned,columns = ['region'],drop_first=True)
df_cleaned = df_cleaned.astype(int)
# print(df_cleaned.head())

#Feature Engineering and Extraction
df_cleaned['bmi_category'] = pd.cut(
    df_cleaned['bmi'],
    bins=[0,18.5,24.9,29.9, float('inf')],
    labels= ['underweight','normal','overweight','obese']
)
df_cleaned = pd.get_dummies(df_cleaned,columns = ['bmi_category'],drop_first=True)
df_cleaned = df_cleaned.astype(int)

# print(df_cleaned.head())

# print(df_cleaned.columns)

from sklearn.preprocessing import StandardScaler
cols = ['age','bmi','children']
scaler = StandardScaler()
df_cleaned[cols] = scaler.fit_transform(df_cleaned[cols])
# list of the feature to check against the target
selected_features = ['age', 'is_female', 'bmi', 'children', 'is_smoker', 'charges',
       'region_northwest', 'region_southeast',
       'region_southwest', 'bmi_category_normal',
       'bmi_category_overweight', 'bmi_category_obese']
from scipy.stats import pearsonr
correlations = {
    feature :pearsonr(df_cleaned[feature],df_cleaned['charges'])[0] 
     for feature in selected_features
       }
correlation_df = pd.DataFrame(list(correlations.items()), columns=['Feature', 'Pearson Correlation'])
correlation_df.sort_values(by='Pearson Correlation', ascending=False)
from scipy.stats import chi2_contingency
import pandas as pd

alpha = 0.05

df_cleaned['charges_bin'] = pd.qcut(df_cleaned['charges'], q=4, labels=False)
chi2_results = {}
cat_features = [
    'is_female', 'is_smoker',
    'region_northwest', 'region_southeast', 'region_southwest',
    'bmi_category_Normal', 'bmi_category_Overweight', 'bmi_category_Obese'
]
for col in cat_features:
    if col not in df_cleaned.columns:
        print(f"{col} not found")
        continue
    contingency = pd.crosstab(df_cleaned[col], df_cleaned['charges_bin'])
    chi2_stat, p_val, _, _ = chi2_contingency(contingency)
    decision = 'Reject Null (Keep Feature)' if p_val < alpha else 'Accept Null (Drop Feature)'
    chi2_results[col] = {
        'chi2_statistic': chi2_stat,
        'p_value': p_val,
        'Decision': decision
    }

chi2_df = pd.DataFrame(chi2_results).T
chi2_df = chi2_df.sort_values(by='p_value')
print(chi2_df)

# final_df = df_cleaned[['age', 'is_female', 'bmi', 'children', 'is_smoker', 'charges','region_southeast','bmi_category_Obese']]
# print(final_df)

final_df = df_cleaned[
    [
        'age',
        'is_female',
        'bmi',
        'children',
        'is_smoker',
        'charges',
        'region_southeast',
        'bmi_category_obese'
    ]
]

# print(final_df)
from sklearn.model_selection import train_test_split
X = final_df.drop('charges',axis = 1)
y = final_df['charges']

X_train, X_test, y_train, y_test = train_test_split(
   X, y, test_size=0.20, random_state=42)

from sklearn.linear_model import LinearRegression
model  = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

# print(y_pred)

from sklearn.metrics import r2_score
r2 = r2_score(y_test,y_pred)
n = X_test.shape[0]
p = X_test.shape[1]

adjusted_r2 = 1- ((1-r2)* (n-1) / (n-p-1))
print(adjusted_r2)