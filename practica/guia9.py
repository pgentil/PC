#!/usr/bin/env python
import typing
import numpy as np

#%%Ej 1
class Coordinates:
    def __init__(self,x_coord: float, y_coord: float):
        self.coordinate = (float(x_coord), float(y_coord))
        self.x, self.y = self.coordinate

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def distance(self, coordinates: 'Coordinates') -> float:
        distance = (((coordinates.get_x() - self.x)**2) + ((coordinates.get_y()) - self.y)**2) ** 0.5
        return distance 

    def get_norm(self):
        norm = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        return norm

    def get_angle(self):



    

