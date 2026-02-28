import pandas as pd
import os

FILE_NAME = "expenses.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns = ["Date", "Category", "Description", "Amount"])
        df.to_csv(FILE_NAME, index = False)

def add_expense():
    date = int(input("Enter the date:"))
    category = input("Enter category of the expense:\n(e.g. such as Food, Rent, Education, Health etc.)")
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

def update_expenses():
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        print(df)

    try:
        user_input = input("Enter the index number to update (or press Enter/'q' to update nothing):")
        if not user_input or user_input.lower == 'q':
            print("Update Cancelled. No changes made.")
            return 
        index = int(user_input)
        df.at[index, 'Date'] = input(f"New Date ({df.at[index, 'Date']}):") or df.at[index, 'Date']
        df.at[index, 'Category'] = input(f"New Category ({df.at[index, 'Category']}):") or df.at[index, 'Category']
        df.at[index, 'Description'] = input(f"New Description ({df.at[index, 'Description']}):") or df.at[index, 'Description']
        

        new_amount = float(input(f"New Amount ({df.at[index, 'Amount']}):"))
        df.at[index, 'Amount'] = float(new_amount) if new_amount else df.at[index, 'Amount']

        df.to_csv(FILE_NAME, index=False)
        print("Update successful!")
    except Exception as e:
        print(f"Error: {e}. Make sure to enter the existing index in the project.")
    else:
        print("No file found")

def delete_expenses():
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        print(df)

        try:
            index = int(input("Enter the index number to delete:"))
            df = df.drop(index)
            df.to_csv(FILE_NAME, index = False)
            print("Expense deleted sucessfully!")
        except:
            print("Invalid index. Nothing was deleted.")
    else:
        print("No records found to delete.")

def main():
    init_file()
    while True:
        print(f"1. Add Expense\n2. View Expense\n3. Update Expense\n4. Delete Expense\n5. Exit")
        choice = int(input("Select an option:"))

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            update_expenses()
        elif choice == 4:
            delete_expenses()
        elif choice == 5:
            break
        else:
            print("Invalid choice!\nTry again.")

if __name__ == "__main__":
    main()