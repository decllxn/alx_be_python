#!/usr/bin/env python3
# Author - Declan Munene
# Date - 19/07/2024
# Description - A script that models a book with attributes for the title, author and publication year

class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"


