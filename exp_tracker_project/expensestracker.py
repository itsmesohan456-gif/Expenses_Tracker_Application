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

