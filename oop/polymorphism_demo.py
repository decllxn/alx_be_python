#!/usr/bin/env python3
# Author - Declan Munene
# Date - 19/07/2024
# Description - Script that utilizes polymorphism and method overriding to calculate area of various shapes
import math


class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
