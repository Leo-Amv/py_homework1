# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
try:
    n = int(input('\nEnter coordinate plane quarter number from 1 to 4:\t'))
    if n == 1:
        print('\nRange of possible coordinates:\n\tx > 0 (from 0 to + ∞)\n\ty > 0 (from 0 to + ∞)\n')
    elif n == 2:
        print('\nRange of possible coordinates:\n\tx < 0 (from - ∞ to 0)\n\ty > 0 (from 0 to + ∞)\n')
    elif n == 3:
        print('\nRange of possible coordinates:\n\tx < 0 (from - ∞ to 0)\n\ty < 0 (from - ∞ to 0)\n')
    elif n == 4:
        print('\nRange of possible coordinates:\n\tx > 0 (from 0 to + ∞)\n\ty < 0 (from - ∞ to 0)\n')
    else:
        print('\nYou must enter number from 1 to 4 ! Try again.\n')
except ValueError:
    print('\nIncorrect data, you must enter number, try again!\n')
