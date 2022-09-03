# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
from math import sqrt, pow
try:
    x1 = int(input('\nEnter coordinate X point A: \t'))
    y1 = int(input('Enter coordinate Y point A: \t'))
    x2 = int(input('\nEnter coordinate X point B:\t'))
    y2 = int(input('Enter coordinate Y point B:\t'))
    print(f'\nWe got two points:\n\tA({x1},{y1})\tB({x2},{y2})')
    distance = sqrt(pow((x2-x1), 2) + pow((y2-y1), 2))
    print(f'\nDistance between two points: {round(distance,3)}\n')
except ValueError:
    print('\nIncorrect data, you must enter number, try again!\n')
