#!/usr/bin/env python3
# Author - Declan Munene
# Date - 24/06/2024
# Description - This is a simple calculator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
math_operation = str(input("Choose the operation (+,-,*,/): "))

match math_operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case _:
        print("Invalid operation")

