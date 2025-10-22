#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#


from src.functions import (generate_expenses, add_a_new_expense,
                           display_expense_property, filter_expenses,remove_expenses,undo)


def get_valid_integer(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Please enter a number greater than or equal to {min_value}.")
            elif max_value is not None and value > max_value:
                print(f"Please enter a number less than or equal to {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_valid_category():
    valid_categories = ["housekeeping", "food", "transport", "clothing", "internet", "others"]
    while True:
        category = input(f"Enter the category ({', '.join(valid_categories)}): ").strip()
        if category in valid_categories:
            return category
        else:
            print(f"Invalid category. Please choose from: {', '.join(valid_categories)}")

def option2(history,expenses):
    print("Do you want to add an expense to the current day? (yes/no)")
    add_to_current_day = input().strip().lower() == "yes"

    day = None
    if not add_to_current_day:
        day = get_valid_integer("Enter the day: ", 1, 30)

    amount = get_valid_integer("Enter the amount: ", 0)
    category = get_valid_category()

    add_a_new_expense(history, expenses, amount, category, day)
    print("Expense added successfully.")

def option3(history,expenses):
    print("Do you want to remove expenses for a specific day? (yes/no)")
    by_day = input().strip().lower() == "yes"
    day = None
    if by_day:
        day = get_valid_integer("Enter the day: ", 1, 30)

    print("Do you want to remove expenses between two days? (yes/no)")
    by_range = input().strip().lower() == "yes"
    start_day = None
    end_day = None
    if by_range:
        start_day = get_valid_integer("Enter the start day: ", 1, 30)
        end_day = get_valid_integer("Enter the end day: ", 1, 30)

    print("Do you want to remove expenses for a specific category? (yes/no)")
    by_category = input().strip().lower() == "yes"
    category = None
    if by_category:
        category = get_valid_category()


    remove_expenses(history, expenses, day=day, start_day=start_day, end_day=end_day, category=category)
    print("The specified expenses have been removed.")


def option4(expenses):
    print("Do you want to display the expenses of a category? (yes/no)")
    by_category = input().strip().lower() == "yes"
    category = None
    if by_category:
        category = get_valid_category()

    print("Do you want to display the expenses with an amount of money? (yes/no)")
    by_amount = input().strip().lower() == "yes"
    operator = None
    value = None
    if by_amount:
        operator = input("Enter the operator (<, >, =): ").strip()
        while operator not in ["<", ">", "="]:
            print("Invalid operator. Please choose <, >, or =.")
            operator = input("Enter the operator (<, >, =): ").strip()

        value = get_valid_integer("Enter the value: ", 0)

    display_expense_property(expenses, category, operator, value)

def option5(history,expenses):
    print("Do you want to filter by category? (yes/no)")
    by_category = input().strip().lower() == "yes"
    category = None
    if by_category:
        category = get_valid_category()

    print("Do you want to filter by amount? (yes/no)")
    by_amount = input().strip().lower() == "yes"
    operator = None
    value = None
    if by_amount:
        operator = input("Enter the operator (<, >, =): ").strip()
        while operator not in ["<", ">", "="]:
            print("Invalid operator. Please choose <, >, or =.")
            operator = input("Enter the operator (<, >, =): ").strip()

        value = get_valid_integer("Enter the value: ", 0)


    filter_expenses(history, expenses, category, operator, value)
    print("Expenses filtered successfully.")

def print_menu():
    print("1.Display the expenses")
    print("2.Add a new expense")
    print("3.Modify expenses")
    print("4.Display expenses with different properties")
    print("5.Filter expenses")
    print("6.Undo")
    print("0.Exit")

def menu():
    expenses=generate_expenses(10)
    history = []
    while True:
        print_menu()

        try:
            option = int(input("Enter your option: "))
            if option==0:
                break
            elif option==1:
                display_expense_property(expenses)

            elif option==2:
                option2(history,expenses)

            elif option==3:
                option3(history,expenses)

            elif option==4:
                option4(expenses)

            elif option==5:
                option5(history,expenses)

            elif option==6:
                expenses=undo(history,expenses)
                print("Undo successfully.")

            else:
                print("Invalid option.")

        except (ValueError, TypeError) as e:
                print("Invalid input.Enter a number.")




