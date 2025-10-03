import csv
import os
from datetime import datetime

EXPENSE_FILE = "expense.csv" 

def init_file():
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Note"])

def add_expense():
    category = input("Enter Category(Food/Travel/Shopping/Other): ")
    amount = input("Enter Amount: ")
    note = input("Enter Note: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(EXPENSE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, note])
        print("Expense added sucesfully")

def view_expenses():
    if not os.path.exists(EXPENSE_FILE):
        print("No expenses found. \n")
        return
    with open(EXPENSE_FILE, "r") as f:
        reader = csv.reader(f)
        expenses = list(reader)

    if len(expenses) <= 1:
        print("No expenses found.\n")
    else:
        print("\n Your Expenses")
        for row in expenses:
            print(" | ". join(row))
            print()
        
def total_expenses():
    if not os.path.exists(EXPENSE_FILE):
        print("No expenses found. \n")
        return
    total = 0
    with open(EXPENSE_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            total += float(row[2])
            print(f"Total Expenses: {total}\n")

def search_expenses():
    keyword = input("Enter category to search: ").lower()
    with open(EXPENSE_FILE, "r")as f:
        reader = csv.reader(f)
        next(reader)
        found = False
        for row in reader:
            if keyword in row[1].lower():
                print(" | ". join(row))
                found = True
            if not found:
                print("No expenses found in this category.\n")
        
def main():
    init_file()
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Search Expense")
        print("4. Total Expense")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expenses()
        elif choice == "4":
            total_expenses
        elif choice == "5":
            print("Exiting Expense Tracker. Good bye")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()                    
