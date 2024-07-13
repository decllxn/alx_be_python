#!/usr/bin/bash
# Author - Declan Munene
# Date - 13/7/2024
# Description - A script that manages a bank account

class BankAccount:
    def __init__(self, account_balance=0): # Default value set to zero
        self.account_balance = account_balance

    def deposit(self, amount):
        self.amount = amount
        return self.account_balance += self.amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self, result):
        self.result = result
        return f"Your account balance is: {self.account_balance}"
