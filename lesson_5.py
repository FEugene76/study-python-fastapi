#**Завдання 1: Робота з функціями**

import calculator

a = input('Введіть число 1: ')
if a.replace('.', '', 1).isdigit():
    a = float(a)
else:
    print(a, 'не є числом')
    exit()

b = input('Введіть число 2: ')
if b.replace('.', '', 1).isdigit():
    b = float(b)
else:
    print(b, 'не є числом')
    exit()

print(f'Введені значення: перше - {a}, друге - {b}')
print('======================')
sum_num = calculator.add(a, b)
print('Сума значень:', sum_num)
sub_num = calculator.subtract(a, b)
sub_num_mod = abs(sub_num)
print('Різниця та віднімання:', sub_num_mod, 'та', sub_num)
mult_num = calculator.multiply(a, b)
print('Множення:', mult_num)
if b == 0:
    print('Поділ на 0 неможливий')
else:
    div_num = calculator.divide(a, b)
    print('Поділ:', div_num)
