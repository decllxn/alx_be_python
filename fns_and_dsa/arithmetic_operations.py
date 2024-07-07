#!/usr/bin/env python3
# Author - Declan Munene
# Date - 7/7/2024
# Description - script to define a function that perfoms basic arithmetic operations

def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return "Math Error"
            elif num2 !== 0:
                return num1 / num2
        case _:
            return "Invalid operater"

