#!/usr/bin/bash
# Author - Declan Munene
# Date - 13/7/2024
# Description - A script that manages a bank account

# bank_account.py

class BankAccount:
    def __init__(self, account_balance=0):  # Default value set to zero
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

