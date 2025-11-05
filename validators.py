from datetime import datetime

def get_valid_date():
    # Prompt user for a valid date (YYYY-MM-DD).
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD.")

def get_valid_amount():
    # Prompt user for a positive numeric amount.
    while True:
        try:
            amount = float(input("Enter amount: ").strip())
            if amount <= 0:
                print("❌ Amount must be greater than zero.")
            else:
                return amount
        except ValueError:
            print("❌ Please enter a valid numeric value.")

def get_valid_category():
    while True:
        category = input("Enter catrgory: ").strip()
        if category:
            return category
        print("❌ Category cannot be empty.")