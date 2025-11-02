from tabulate import tabulate

def show_summary(expenses):
    if not expenses:
        print("No data available.")
        return
    category_totals={}
    for e in expenses:
        category_totals[e["category"]]= category_totals.get(e["category"],0)+e["amount"]

    month_totals = {}
    for e in expenses:
        month = e["date"][:7]
        month_totals[month] = month_totals.get(month,0)+e["amount"]
    
    print("\n Expenses by category:\n")
    print(tabulate(category_totals.items(), headers=["Category","Total "], tablefmt="grid"))
    print("\nExpense by month:\n")
    print(tabulate(month_totals.items(), headers=["Month","Total"], tablefmt="grid"))
