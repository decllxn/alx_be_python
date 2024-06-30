#!/usr/bin/env python3
# Author - Declan Munene
# Date - 30/6/2024
# Description - Pattern drawing

size = int(input("Enter the size of the pattern: "))
i = 0
while i < size:
    for j in range(size):
        print("*", end="")
    print()
    i += 1
