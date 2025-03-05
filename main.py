print("Welcome to the Student Expense Tracker!")
expenses = []
def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})
    print(f"Added: ₹{amount} in {category}")

add_expense(500, "Rent")
print(expenses)
