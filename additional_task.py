def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)


try:
    n = int(input('\nEnter number "N" from 0 to 30 :\t'))
    if 0 <= n <= 30:
        for i in range(n+1):
            print(f'Fibonacci({i}) = {fibonacci(i)}')
        print(f'\nResult:\tFibonacci({n}) =\t{fibonacci(n)}\n')
    else:
        print('\nYou must enter number "N" from 0 to 30, try again!\n')
except ValueError:
    print('\nIncorrect data, you must enter number, try again!\n')
