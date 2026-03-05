import pandas as pd
import matplotlib.pyplot as plt
import os
df = pd.read_csv("personal_expense_dataset.csv")

print("Dataset Loaded Successfully")
df.head()
# Check missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert Month column to string if needed
df["Month"] = df["Month"].astype(str)
expense_categories = [
    "Food","Groceries","Transport","Entertainment",
    "Shopping","Rent","Bills","Healthcare","Education"
]

category_avg = df[expense_categories].mean()

print("\nAverage Expense Per Category")
print(category_avg)
plt.figure(figsize=(10,6))

category_avg.sort_values().plot(kind="bar")

plt.title("Average Spending by Category")
plt.xlabel("Expense Category")
plt.ylabel("Average Amount")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
monthly_expense = df.groupby("Month")["Total_Expenses"].mean()

plt.figure(figsize=(10,6))

plt.plot(monthly_expense.index,
         monthly_expense.values,
         marker="o")

plt.title("Monthly Expense Trend")
plt.xlabel("Month")
plt.ylabel("Average Expense")

plt.grid(True)
plt.show()
