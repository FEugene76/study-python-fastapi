### Списки:
print('\n1. **Робота із списками:**')
#Завдання: Створіть список чисел. Додайте до списку числа 10 і 20,
# видаліть число 10 і виведіть отриманий список.
list = [10, 20]
list.remove(10)
print(list)

print('\n2. **Знаходження суми:**')
#Завдання: Створіть список чисел. Знайдіть та виведіть суму всіх чисел у списку.
list = [10, 20, 30, 40, 50]
res = 0
for val in list:
    res += val
print('Сумма чисел у списку -', res)

print('\n3. **Подвійні значення:**')
#Завдання: Створіть список чисел. Подвойте кожне число у списку та виведіть результат.
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [x * 2 for x in numbers]
print(numbers)
print(doubled_numbers)

### Кортежі:
print('\n1. **Робота із кортежами:**')
#Завдання: Створіть кортеж з трьох різних предметів, таких як ("яблуко", "банан", "апельсин").
# Виведіть кожен елемент кортежу окремо.
tup_1 = ("яблуко", "банан", "апельсин")
print('Елементи кортежу:')
for x in tup_1:
    print('-->', x)

print("\n2. **Об'єднання кортежів:**")
#Завдання: Створіть два кортежі з числами і об'єднайте їх у новий кортеж. Виведіть отриманий кортеж.
tup_1 = ("яблуко", "банан", "апельсин")
tup_2 = ("томат", "огiрок", "капуста")
tup_3 = tup_1 + tup_2
print(tup_3)

### Словники:
print('\n1. **Робота із словниками:**')
#Завдання: Створіть словник, що містить інформацію про вашого улюбленого спортсмена
#(ім'я, вік, спорт, команда тощо). Виведіть цю інформацію на екран.
s_men = {'name': 'Пол Гаскойн', 'age': '62', 'sport': 'Футбол', 'team': 'Эвертон, GB'}
print(' Имя:', s_men.get('name'), '\n',
      'Вiк:', s_men.get('age'), '\n',
      'Спорт:', s_men.get('sport'), '\n',
      'Команда:', s_men.get('team')
)

print('\n2. **Оновлення словника:**')
#Завдання: Створіть словник, що містить ваші улюблені книги (назва книги та рік видання).
#Додайте до словника нову улюблену книгу та виведіть оновлений словник.
books = {'Mein Kampf': 1925,
         'Der Wille zur Macht': 1901
}
books.update({"Незнайка на Луне":1965})
for key, value in books.items():
    print('Назва книги:',key, '--> Рiк видання:',value)

print('\n3. **Пошук значення:**')
#Завдання: Створіть словник, що містить інформацію про країни та їх столиці. Запитайте
#користувача про назву країни і виведіть столицю цієї країни (якщо така країна є у словнику).
countries = {'Германія': 'Берлін',
             'Великобританія': 'Лондон',
             'США': 'Вашингтон',
             'Японія': 'Токіо'
}
requested = 'Японія'
print('Запрос 1:', requested)

if countries.get(requested) is not None:
    print(f'Страна {requested} є в словнику.')
    print('Столиця:', countries[requested])
else:
    print(f'Страни {requested} немає в словнику.')

requested1 = 'Зімбабве'
print('\nЗапрос 2:', requested1)

if countries.get(requested1) is not None:
    print(f'Страна {requested1} є в словнику.')
    print('Столиця:', countries[requested])
else:
    print(f'Страни {requested1} немає в словнику.')