# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
print('\nCoordinates X and Y must be non-zero\n')
try:
    x = int(input('Enter coordinate X:\t'))
    y = int(input('Enter coordinate Y:\t'))

    n = 0
    if x > 0 and y > 0:
        n = 1
    elif x < 0 and y > 0:
        n = 2
    elif x < 0 and y < 0:
        n = 3
    elif x > 0 and y < 0:
        n = 4
    else:
        print('\nOne of the coordinates is 0 ! Try again.')
    print(f'\nCoordinate plane quarter number: {n}\n')
except ValueError:
    print('\nIncorrect data, you must enter number, try again!\n')
