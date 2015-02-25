"""
    Author: Orens Xhagolli
    File: legal.py
    Description: Contains functions that check whether expressions are legal.
"""

import prefix


def check(exp):
    """
    Performs all available checks on an expression.
    :param exp: Expression in string form.
    :return: True if the expression is legal, False otherwise.
    """
    if (not balance_check(exp)) : # add other statements as 'or' statements
        return False
    return True


def balance_check(exp):
    """
    Checks the balance of parentheses in an expression.
    :param exp: Expression in string form.
    :return: True if parentheses are balanced, False otherwise.
    """
    left = 0
    right = 0
    for ch in exp:
        if ch == '(':
            left += 1
        if ch == ')':
            right += 1
    if left == right:
        return True
    else:
        print("Error: Unbalanced parentheses!")
        return False

def paren_check(exp):
    """
    Checks whether there is meaning to the parentheses in an expression.
    :param exp: Expression in string form.
    :return: True if parentheses are meaningful, False otherwise.
    """
    ref = exp
    # Is the token a function?
    for i in prefix.supported_func():
        while i in ref:
            index = ref.find()
            par_index = index + len(i)
            if ref[par_index] == "(" and ref[par_index+1] == ")":
                print("Error: iqMath Functions take at least one argument")
                return False
            ref.replace(i, '')

    for j in range(0, len(ref)):
        if (ref[j] == "(" or ref[j] == ")") and (ref[j+1] == ")" or ref[j+1] == "("):
            print("Error: Please use prefix or infix (operators) functions.")
            return False
    return True