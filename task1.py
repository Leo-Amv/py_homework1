# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
day = int(input('Enter day of the week number from 1 to 7:\t'))
if day < 1 or day > 7:
    print('\nIncorrect data try enter number from 1 to 7!\n')
elif day == 6 or day == 7:
    print('Yes')
else:
    print('No')
