# Input file
from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    # Put today if nothing is entered
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    # Validate format
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError:
        print(ValueError)
        return get_amount()
    
def get_category():
    catergory = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if catergory in CATEGORIES:
        return CATEGORIES[catergory]
    print("Invalid category please enter 'I' for Income or 'E' for Expense.")
    return get_category()

def get_description():
    return input("Enter a description (optional): ")