# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
list = ["X", "Y", "Z"]
values = []
print('\nEnter values ​​such as 0 or 1, where 0 is false and 1 is true\nStatement : ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z\n')
for i in range(3):
    values.append(int(input(f'Enter {list[i]}:\t')))
expression1 = not (values[0] or values[1] or values[2])
print(f'\n¬(X ⋁ Y ⋁ Z) = {expression1}')
expression2 = not values[0] and not values[1] and not values[2]
print(f'¬X ⋀ ¬Y ⋀ ¬Z = {expression2}')
if expression1 == expression2:
    print('\nThe statement is True\n')
else:
    print('\nThe statement is False\n')
