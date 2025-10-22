#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#

from random import randint
from texttable import Texttable
from copy import deepcopy
current_day=22

def create_expense(day:int, amount_of_money:int, expense_type:str)->list:
    """
    Creates a new expense entry.

    Parameters:
    -day (int): The day of the expense (1 ≤ day ≤ 30).
    -amount_of_money (int): The amount of the expense (≥ 0).
    -expense_type (str): The category/type of the expense.

    Returns : A list representing an expense: [day, amount_of_money, expense_type].
     """

    if type(day)!=int or day<1 or day>30:
        raise TypeError("Day must be an integer between 1 and 30.")
    if type(amount_of_money)!=int or amount_of_money<0:
        raise TypeError("Amount of money must be a positive integer.")
    if type(expense_type)!=str :
        raise TypeError("Expense type must be a string .")
    return [day, amount_of_money, expense_type]

def get_expense_day(expense):
    return expense[0]

def get_expense_amount_of_money(expense):
    return expense[1]

def get_expense_type(expense):
    return expense[2]

def to_str(expense):
    day=get_expense_day(expense)
    amount_of_money=get_expense_amount_of_money(expense)
    expense_type=get_expense_type(expense)
    return day, amount_of_money, expense_type

def generate_expenses(n:int):
    result=[]

    for i in range(n):
        day=randint(1,30)
        amount_of_money=randint(1,1000)
        list_of_expenses = ["housekeeping", "food", "transport", "clothing", "internet", " others"]
        expense_index=randint(0,len(list_of_expenses)-1)
        expense_type=list_of_expenses[expense_index]
        expense=create_expense(day,amount_of_money,expense_type)
        result.append(expense)

    return result




def add_a_new_expense(history,expenses: list, amount_of_money: int, expense_type: str, day: int = None) -> list:
    """
     Adds a new expense to the expenses list. If day is not provided, the expense is added for the current day.

    Parameters:
    -history (list): A list where previous states of expenses are saved for undo functionality.
    -expenses (list): The list of all expenses.
    -amount_of_money (int): The amount for the new expense.
    -expense_type (str): The category/type of the new expense.
    -day (int, optional): The day for the expense. If None, defaults to the current day.

    Returns:The updated list of expenses.


     """
    global current_day
    save_state(history, expenses)
    if day is None:
        day = current_day  # Default to current day if no day is provided

    new_expense = create_expense(day, amount_of_money, expense_type)
    expenses.append(new_expense)
    return expenses

def remove_expenses(history,expenses:list, day:int=None, start_day:int=None, end_day:int=None, category:str=None):
    """
    Removes expenses based on the specified criteria.

    Parameters:

    -history (list): A list where previous states of expenses are saved for undo functionality.
    -expenses (list): The list of all expenses.
    -day (int, optional): Removes all expenses for this specific day.
    -start_day, end_day (int, optional): Removes all expenses between these days (inclusive).
    -category (str, optional): Removes all expenses for this specific category.

    Returns:The updated list of expenses after removal.

    """
    save_state(history, expenses)
    for i in range(len(expenses)-1,-1,-1):
        if day is not None and get_expense_day(expenses[i]) == day:
            expenses.pop(i)
        elif start_day is not None and end_day is not None:
            if start_day>end_day:
                start_day, end_day = end_day, start_day
            if start_day<=get_expense_day(expenses[i])<=end_day:
                expenses.pop(i)
        elif category is not None and get_expense_type(expenses[i]) == category:
            expenses.pop(i)

    return expenses


def display_expense_property(expenses:list, category:str=None, operator:str=None, value:int=None):
    """
    Displays the expenses based on specified filtering criteria such as category and/or amount.

    Parameters:
    -expenses (list): The list of all expenses.
    -category (str, optional): If provided, filters expenses by this category.
    -operator (str, optional): A comparison operator for filtering the amount ("=", "<", ">").
    -value (int, optional): The value to compare the amount of money with.

    Prints the filtered expenses to the console. If no expenses match the criteria, prints a "No expenses found." message.
     """
    table = Texttable()

    table.add_row(["Day", "Amount", "Category"])

    for expense in expenses:
        day=get_expense_day(expense)
        amount_of_money=get_expense_amount_of_money(expense)
        expense_type=get_expense_type(expense)

        if category is not None and expense_type != category:
            continue


        if operator is not None and value is not None:
            if operator == ">" and not(amount_of_money > value):
                continue
            if operator == "<" and not (amount_of_money < value):
                continue
            if operator =="=" and  not(amount_of_money == value):
                continue

        table.add_row([day, amount_of_money, expense_type])

    print(table.draw())

def filter_expenses(history,expenses:list,category:str=None, operator:str=None, value:int=None):
    """
    Filters the expenses based on specified criteria, and saves the current state for undo functionality.

    Parameters:
    -history (list): A list where previous states of expenses are saved for undo functionality.
    -expenses (list): The list of all expenses.
    -category (str, optional): If provided, filters expenses by this category.
    -operator (str, optional): A comparison operator for filtering the amount ("=", "<", ">").
    -value (int, optional): The value to compare the amount of money with.

    Returns:The filtered list of expenses.

      """
    save_state(history, expenses)
    for i in range(len(expenses)-1,-1,-1):
        amount_of_money=get_expense_amount_of_money(expenses[i])
        expense_type=get_expense_type(expenses[i])
        if category is not None and expense_type != category:
            expenses.pop(i)

        if operator is not None and value is not None:
            if operator ==">" and not(amount_of_money > value):
                expenses.pop(i)
            if operator =="<" and not (amount_of_money < value):
                expenses.pop(i)
            if operator =="=" and not(amount_of_money == value):
                expenses.pop(i)
    return expenses

def save_state(history, expenses):
    """
    Saves the current state of expenses to the history stack for undo functionality.

    Parameters:
    -history (list): A list where previous states of expenses are saved.
    -expenses (list): The current list of expenses.
    """
    history.append(deepcopy(expenses))


def undo(history, expenses, steps=1):
    """
    Reverts the last `steps` operations that modified the expenses list by restoring previous states from history.

    Parameters:
    - history (list): A list of previous states of expenses.
    - expenses (list): The current list of expenses.
    - steps (int): The number of undo steps to perform (default is 1).

    Returns:
    - The list of expenses after restoring the previous state(s).
    """
    if steps < 1:
        raise ValueError("Number of undo steps must be at least 1.")

    if steps > len(history):
        print(f"Only {len(history)} actions available to undo. Undoing all available actions.")
        steps = len(history)

    for _ in range(steps):
        if history:  # Ensure history is not empty
            expenses.clear()
            expenses.extend(history.pop())
        else:
            print("No more actions to undo.")
            break

    return expenses


#Tests for all non-UI functions related to functionalities (A) and (B)
def test_add_a_new_expense():
    history = []
    expenses = []

    global current_day
    current_day = 21

    expenses = add_a_new_expense(history, expenses, amount_of_money=100, expense_type="food")
    expenses = add_a_new_expense(history, expenses, amount_of_money=200, expense_type="transport", day=15)
    expenses=add_a_new_expense(history,expenses, amount_of_money=80, expense_type="clothes",day=3)
    expenses=add_a_new_expense(history,expenses, amount_of_money=520, expense_type="others", day=28)

    assert len(expenses) == 4
    assert len(history) == 4
    assert expenses[0] == [21,100, "food"]
    assert expenses[1] == [15, 200, "transport"]
    assert expenses[2] == [3, 80, "clothes"]
    assert expenses[3] == [28, 520, "others"]


    assert history[0] == []
    assert history[1] == [[21, 100, "food"]]
    assert history[2] == [[21, 100, "food"],[15,200,"transport"]]
    assert history[3] == [[21, 100, "food"],[15,200,"transport"],[3,80,"clothes"]]


def test_remove_expenses():
    history = []
    expenses = [
        [21, 100, "food"],
        [15, 200, "transport"],
        [10, 50, "food"],
        [5, 75, "internet"]
    ]


    updated_expenses = remove_expenses(history, expenses, day=21)
    assert len(updated_expenses) == 3
    assert [21, 100, "food"] not in updated_expenses
    assert len(history) == 1


    updated_expenses = remove_expenses(history, updated_expenses, start_day=5, end_day=10)
    assert len(updated_expenses) == 1
    assert [10, 50, "food"] not in updated_expenses
    assert [5, 75, "internet"] not in updated_expenses
    assert len(history) == 2


    updated_expenses = remove_expenses(history, updated_expenses, category="transport")
    assert len(updated_expenses) == 0
    assert [15, 200, "transport"] not in updated_expenses
    assert len(history) == 3


test_add_a_new_expense()
test_remove_expenses()









