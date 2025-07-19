expenses = []  # Global list to store expense dictionaries

def add_expense():
    
    
def view_total():
   
    

def list_expenses():
    
    if not expenses:
        print("📭 No expenses recorded.\n")
        return
    print(" All Expenses:")
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. ₹{expense['amount']:.2f} - {expense['category']} - {expense['description']}")
    print()

def filter_by_category():
    
    

def main():
    
    print(" Welcome to Expense Tracker")
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

