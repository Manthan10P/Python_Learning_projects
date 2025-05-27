import json
from datetime import datetime

expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    print("✅ Expense added!")

add_expense()
print(expenses)

with open("expenses.json", "w") as file:
    json.dump(expenses, file)

