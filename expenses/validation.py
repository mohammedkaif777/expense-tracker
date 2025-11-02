from datetime import datetime

def get_valid_amount():
    try:
        return float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount! Must be a number.")
        return None

def get_valid_date():
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_input:
        return datetime.today().strftime("%Y-%m-%d")
    try:
        datetime.strptime(date_input, "%Y-%m-%d")
        return date_input
    except ValueError:
        print("Invalid date format.")
        return None
