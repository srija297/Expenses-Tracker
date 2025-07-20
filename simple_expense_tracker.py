import datetime
expenses = []
def add_expense():

    print("Add Expense CLI - Naveena's Task")
    try:
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (e.g., Food, Travel): ")
        description = input("Enter description (optional): ")
        date = input("Enter date (DD-MM-YYYY), or press Enter for today: ")
        date = date if date.strip() else None
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
       
    
        print("\n Saved Expenses:")
        for e in expenses:
            print(e)

    except ValueError:
        print("Invalid input. Amount must be a number.")
        add_expense()


def view_total():
   
    total = sum(expense['amount'] for expense in expenses)
    print( "Total expense:",total)

def list_expenses():
    
    if not expenses:
        print(" No expenses recorded.\n")
        return
    print(" All Expenses:")
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. ₹{expense['amount']:.2f} - {expense['category']} - {expense['description']}")
    print()

# 🔻🔻🔻 FILTER BY CATEGORY FUNCTION START 🔻🔻🔻
def filter_by_category():
    if not expenses:
        print("No expenses to filter.\n")
        return

    category = input("Enter category to filter by: ")
    filtered = [exp for exp in expenses if exp['category'] == category]

    if not filtered:
        print(f"No expenses found for category '{category}'.\n")
    else:
        print(f"\nExpenses in '{category}':")
        for idx, expense in enumerate(filtered, 1):
            print(f"{idx}. ₹{expense['amount']:.2f} - {expense['description']}")
        print()
# 🔺🔺🔺 FILTER BY CATEGORY FUNCTION END 🔺🔺🔺
    

def main():
    
    print(" Welcome to Expense Tracker")
    view_total()
    while True:
        print("1. Add Expense")
        print("2. View Total")
        print("3. List Expenses")
        print("4. Filter by Category")
        print("5. Exit")
        choice = input("Enter your choice: ")
        print()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_total()
        elif choice == '3':
            list_expenses()
        elif choice == '4':
            filter_by_category()
        elif choice == '5':
            print(" Exiting... Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()
