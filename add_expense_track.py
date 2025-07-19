import datetime
expenses = []
def add_expense(amount, category, description="", date=None):
    if date is None:
        date = datetime.datetime.now().strftime("%d-%m-%Y")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)
    print("Expense added successfully!")
if __name__ == "__main__":
    print("Add Expense CLI - Naveena's Task")
    try:
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (e.g., Food, Travel): ")
        description = input("Enter description (optional): ")
        date = input("Enter date (DD-MM-YYYY), or press Enter for today: ")
        date = date if date.strip() else None
        add_expense(amount, category, description, date)
        print("\n Saved Expenses:")
        for e in expenses:
            print(e)

    except ValueError:
        print("Invalid input. Amount must be a number.")
