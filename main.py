expenses =[]

def add_Expense():
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    date = input("Enter Date (YYYY-MM-DD): ")
    expenses.append({"category": category, "amount":amount, "date":date})
    print("Expense added successfully!!")

def view_Expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expenses: ${total}")
    for  exp in expenses:
        print(f"{exp['date']} - {exp['category']}: ${exp['amount']}")

def main():
    print("Welcome To Expense-Daily")
    while True:
        print("\n 1.Add Expense\n 2. View Expense\n3. Exit")
        choice = input("Choose an Option: ")
        if choice == '1':
            add_Expense()
        elif choice == '2':
            view_Expense()
        elif choice == '3':
            break
        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()