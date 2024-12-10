import csv

def add_expense(expenses):
    try:
        date = input("Enter the date of the expense (DD-MM-YYYY): ")
        category = input("Enter the category of the expense (e.g., Food, Travel): ")
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description of the expense: ")

        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }

        expenses.append(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please ensure the amount is a number and try again.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses to display.")
        return

    print("\nStored Expenses:")
    for i, expense in enumerate(expenses, start=1):
        if not all(key in expense and expense[key] for key in ['date', 'category', 'amount', 'description']):
            print(f"Expense {i} is incomplete and will be skipped.")
            continue

        print(f"Expense {i}:")
        print(f"  Date: {expense['date']}")
        print(f"  Category: {expense['category']}")
        print(f"  Amount: {expense['amount']}")
        print(f"  Description: {expense['description']}")
        print("-" * 30)

def set_budget(filename="budget.csv"):
    try:
        budget = float(input("Enter your monthly budget: "))
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['monthly_budget'])
            writer.writeheader()
            writer.writerow({'monthly_budget': budget})
        print(f"Monthly budget set to {budget:.2f} and saved to file.")
        return budget
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return 0

def load_budget(filename="budget.csv"):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                return float(row['monthly_budget'])
    except FileNotFoundError:
        print("No budget file found. Please set a monthly budget by choosing appropriate menu option.")
    except Exception as e:
        print(f"An error occurred while loading the budget: {e}")
    return 0.0

def calculate_total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses if 'amount' in expense)

def check_budget(budget, expenses):
    total_expenses = calculate_total_expenses(expenses)
    print(f"\nBudget: {budget:.2f}")
    print(f"Total Expenses: {total_expenses:.2f}")
    if total_expenses > budget:
        print("Warning: You have exceeded your budget!")
    else:
        remaining = budget - total_expenses
        print(f"You have {remaining:.2f} left for the month.")

def save_expenses_to_csv(expenses, filename="expenses.csv"):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
            writer.writeheader()
            writer.writerows(expenses)
        print(f"Expenses saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving to CSV: {e}")

def load_expenses_from_csv(filename="expenses.csv"):
    expenses = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount'])
                expenses.append(row)
        print(f"Expenses loaded from {filename}.")
    except FileNotFoundError:
        print(f"No existing file found at {filename}. Starting with an empty expenses list.")
    except Exception as e:
        print(f"An error occurred while loading from CSV: {e}")
    return expenses

def main():
    budget = load_budget()  # Load budget on startup
    expenses = load_expenses_from_csv()
    
    while True:
        print("\nMenu:")
        print("1. Set Monthly Budget")
        print("2. Add an Expense")
        print("3. View Expenses")
        print("4. Track Budget")
        print("5. Save Expenses")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            if budget == 0:
                budget = set_budget()
            else:
                print(f"\nCurrent Budget: {budget:.2f}")
                print("Do you want to update the budget:\n 1. YES \n 2. NO")
                choice_b = input("Choose an option:")
                if choice_b == '1':
                   budget = set_budget() 
                else:
                    print(f"\nCurrent Budget: {budget:.2f}")

        elif choice == '2':
            if budget == 0:
                print("Please set a monthly budget first.")
            else:
                add_expense(expenses)
        elif choice == '3':
            if budget == 0:
                print("Please set a monthly budget first.")
            else:
                view_expenses(expenses)
        elif choice == '4':
            if budget == 0:
                print("Please set a monthly budget first.")
            else:
                check_budget(budget, expenses)
        elif choice == '5':
            if budget == 0:
                print("Please set a monthly budget first.")
            else:
                save_expenses_to_csv(expenses)
        elif choice == '6':
            save_expenses_to_csv(expenses)
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
