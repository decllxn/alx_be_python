#!/usr/bin/env python3
# Author - Declan Munene
# Date - 19/07/2024
# Description - A script that manages a collection of books

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = [] # Creating a list, as an attribute

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only Book instances can be added.")

    def list_books(self):
        for book in self.books:
            print(book)
