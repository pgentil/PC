#!/usr/bin/env python
import time
import typing
import numpy as np
import random


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
        norm = self.get_norm()
        angle = np.arccos(self.x/norm) * (180/np.pi)
        return angle
    
    def __repr__(self):
        return f"Coordinates({self.x}, {self.y})"

#%%Ej 7
class GeometryFigure:
    def __init__(self):
        self.sides = []
        pass

    def get_perimeter(self):
        perimeter = 0
        for side in self.sides:
            perimeter += side
        return perimeter

    def __eq__(self, object: object):
        return object.get_perimeter() == self.get_perimeter()

    def __gt__(self, object: object):
        return self.get_perimeter() > object.get_perimeter()
        

    def __lt__(self, object: object):
        return self.get_perimeter() < object.get_perimeter()



#%% Ej 2
class Triangle(GeometryFigure):
    def __init__(self, c1: Coordinates, c2: Coordinates, c3: Coordinates):
        self.sides = [c1.distance(c2), c2.distance(c3), c3.distance(c1)]
        self.vertice1 = c1
        self.vertice2 = c2
        self.vertice3 = c3


    def get_area(self):
        gradiente = (self.vertice2.get_y() - self.vertice1.get_y())/(self.vertice2.get_x() - self.vertice1.get_x())
        altura = (gradiente * (self.vertice3.get_x() - self.vertice1.get_x()) + self.vertice1.get_y() - self.vertice3.get_y())/((((gradiente)**2)+1)**0.5)
        return abs((self.sides[0]*altura)/2)

    def get_perimeter(self):
        perimeter = self.sides[0] + self.sides[1] + self.sides[2]
        return perimeter


    def __repr__(self):
        return f"Triangle({self.vertice1}, {self.vertice2}, {self.vertice3})"

#%%Ej 3
class Rectangle(GeometryFigure):
    def __init__(self, height, length):
        self.area = height * length
        self.sides = [height, height, length, length]
        self.height = height
        self.length = length

    def get_area(self):
        return self.area

    def draw(self):
        first = [2,1,1,1,2]
        second = [3,0,0,0,3]
        third = first
        all = [first, second, third]
        for i in all:
            for j in i:
                if j == 0: print(" ", end="")
                elif j == 1: print("-", end="")
                elif j == 2: print("*", end="")
                elif j == 3: print("|", end="")
            print("")

    def __repr__(self):
        return f"Rectangle({self.height}, {self.length})"


#%%Ej 8
class Interval:
    def __init__(self, initial: float, end: float, step: int=1):
        self.initial = initial
        self.end = end
        self.actual_value = initial
        self.step = step

    def set_step(self, value: float):
        self.step = value

    def get_next(self):
        self.actual_value += self.step
        return self.actual_value

    def has_next(self):
        future_value = self.actual_value + self.step
        if future_value >= self.initial and future_value <= self.end:
            return True
        else: 
            return False


#%%EJ 9
import random

class Scissors:
    def __init__(self):
        pass
    
    def cmp(self, other):
        if isinstance(other, Rock):
            return -1
        elif isinstance(other, Scissors):
            return 0
        else:
            return 1
    
    def __str__(self):
        return 'Scissors'

class Rock:
    def __init__(self):
        pass

    def cmp(self, other):
        if isinstance(other, Rock):
            return 0
        elif isinstance(other, Scissors):
            return 1
        else:
            return -1

    def __str__(self):
        return 'Rock'
    
class Paper:
    def __init__(self):
        pass

    def cmp(self, other):
        if isinstance(other, Rock):
            return 1
        elif isinstance(other, Scissors):
            return -1
        else:
            return 0

    def __str__(self):
        return 'Paper'

def main():
    while True: 
        cpu = random.choice((Rock(), Paper(), Scissors()))

        while True:
            user_choice = input("""Choose one:\n1.Rock\n2.Paper\n3.Scissors\n> """)
            if user_choice == '1':
                user = Rock()
                break
            elif user_choice == '2':
                user = Paper()
                break
            elif user_choice == '3':
                user = Scissors()
                break
            else:
                print("Please try again.")

        resolution = user.cmp(cpu)
        print(f"The computer choice was: {cpu}")
        if resolution == 1:
            print("You've won.")
            break
        if resolution == 0:
            print("It was a tie, AGAIN!")
        elif resolution == -1:
            print("You've lost.")
            break




if __name__ =="__main__":
    # c1 = Coordinates(1, 1)
    # print(c1)
    # print(c1.get_x())
    # print(c1.get_y())
    # print(c1.get_angle())
    # print(c1.get_norm())
    # c2 = Coordinates(4, 1)
    # c3 = Coordinates(2.5, 3)
    # print(c2.distance(c1))
    # triangulo = Triangle(c1, c2, c3)
    # print(triangulo.get_area())
    # rectangulo = Rectangle(5, 3)
    # goc = Rectangle(5, 3)
    # rec.draw()
    # print(rec.get_area())
    # print(rectangulo == goc)

    # interval = Interval(0, 100)
    # interval.set_step(0.5)
    # while interval.has_next():
    #     print(interval.get_next())
    main()

#%%Ej 6
    # def U(a: float = 0, b: float = 10) -> float:
    #     return random.random() * (b - a) + a
    

    
    # lista = [Rectangle(U(), U()) for _ in range(5)] + [Triangle(Coordinates(U(), U()), Coordinates(U(), U()), Coordinates(U(), U())) for _ in range(5)]

    # lista.sort()

    # print(lista)
    # for i in lista:
    #     print (i.get_perimeter())





