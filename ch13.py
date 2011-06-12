#!/usr/bin/env python

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def distance_from_origin(self):
        return((self.x ** 2) + (self.y ** 2)) ** 0.5