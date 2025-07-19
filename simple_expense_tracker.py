

def list_expenses():
    
    if not expenses:
        print("📭 No expenses recorded.\n")
        return
    print(" All Expenses:")
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. ₹{expense['amount']:.2f} - {expense['category']} - {expense['description']}")
    print()

