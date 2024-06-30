#!/usr/bin/env python3
# Author - Declan Munene
# Date - 30/6/2024
# Description - Creating a multiplication table

number = int(input("Enter a number to see the multiplication table: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
