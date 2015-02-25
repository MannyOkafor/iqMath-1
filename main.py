"""
    Author: Orens Xhagolli
    File: main.py
    Description: The program that deals with the interaction.
"""

import legal


def intro():
    print("=== Welcome to iqMath ===")


def main():
    expression = input("iqMath >>> :")
    expression = expression.strip('\n')
    expression = expression.replace(' ', '')
    if legal.check(expression):
        print("Tests passed")


intro()
main()