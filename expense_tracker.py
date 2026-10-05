import csv
import os

FILE_NAME = "expenses.csv"


def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Category", "Amount", "Description"])

        writer.writerow([date, category, amount, description])

    print("Expense added successfully! ✅")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses recorded yet.")
        return

    print("\n========== EXPENSES ==========")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        total = 0

        for expense in reader:
            print(
                f"{expense['Date']} | "
                f"{expense['Category']} | "
                f"₹{expense['Amount']} | "
                f"{expense['Description']}"
            )

            total += float(expense["Amount"])

        print("------------------------------")
        print(f"Total Expenses: ₹{total:.2f}")


def main():
    print("================================")
    print("         EXPENSE TRACKER")
    print("================================")

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                add_expense()
            except ValueError:
                print("Please enter a valid amount!")

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("\nThank you for using Expense Tracker! 💰")
            break

        else:
            print("Invalid choice!")


main()