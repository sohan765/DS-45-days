import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Load dataset
url = "https://raw.githubusercontent.com/sohan765/DS-45-days/main/Employers_data.csv"
df = pd.read_csv(url)
print(df.head())

X = df[["Age", "Experience_Years", "Education_Level"]]
y = df["Salary"]
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["Education_Level"])
    ],
    remainder="passthrough"
)
degree = input("enter the degree")
# Multiple Linear Regression Pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


print("R2 Score :", r2_score(y_test, y_pred))
new_employee = pd.DataFrame({
    "Age": [age],
    "Experience_Years": [year],
    "Education_Level": []
})

predicted_salary = model.predict(new_employee)

print("Predicted Salary = ₹", round(predicted_salary[0], 2))

# -----------------------------
# Pie Chart: Employees by Department
# -----------------------------
dept_count = df["Department"].value_counts()

plt.figure(figsize=(7,7))
plt.pie(
    dept_count,
    labels=dept_count.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Employee Distribution by Department")
plt.show()

plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red"
)

plt.xlabel("Actual Salary")
plt.ylabel("Predicted Salary")
plt.title("Multiple Linear Regression (Salary Prediction)")
plt.show()