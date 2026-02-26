import pandas as pd
import os

FILE_NAME = "expenses.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns = ["Date", "Category", "Description", "Amount"])
        df.to_csv(FILE_NAME, index = False)

def add_expense():
    date = int(input("Enter the date:"))
    category = input("Enter category of the expense:\n(e.g. such as Food, Rent, Education, Health etc.")
    description = input("Enter the description of the expense:")
    amount = float(input("Enter the expense amount:"))

    new_data = pd.DataFrame([[date, category, description, amount]])

    new_data.to_csv(FILE_NAME, mode = 'a', header=False, index=False)
    print("Expense was added successfully into the expense tracker!\n")

def view_expenses():
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        print("\n--- Your Expenses ---")
        print(df)
        print(f"Total Spent: {df['Amount'].sum()}\n")
    else:
        print("Error! No records found here.")

def main():
    init_file()
    while True:
        print(f"1. Add Expense\n2. View Expense\n3. Exit")
        choice = int(input("Select an option:"))

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            break
        else:
            print("Invalid choice!\nTry again.")

if __name__ == "__main__":
    main()