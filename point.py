#!/usr/bin/env python

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        

    def __str__(self):
        return ("(%i, %i)") % (self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y


    def __rmul__(self, other):
        return Point(other * self.x, other * self.y)


    def distance_from_origin(self):
        return((self.x ** 2) + (self.y ** 2)) ** 0.5
