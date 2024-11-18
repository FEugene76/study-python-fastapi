#Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
num_str =  125 #<class 'int'>
num_str = str(num_str)
print(type(num_str))

#Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити
#усі букви 'y' на '0' та 'i' на '1'.
message = 'Hi, my name is Python!'
message_new = message.replace('y', '0').replace('i', '1')
print(message_new)

#3. Cтворити зміну split_test = 'This is a split test' і розділити її по
# пробілах за допомогою функції split(), а потім знову обʼєднати у строку
# за допомогою функції join() у змінну string_join
split_test = 'This is a split test'
splitted = split_test.split()
print(splitted)
joined = ' '.join(splitted)
print(joined)

#4. Визначити довжину рядку string_join за допомогою функції len()
print(len(joined))

#Робота зі списками:
#1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції
# append() додати туди спочатку 4, а потім 5
list_append = [1, 2, 3]
list_append.append(4)
print(list_append)
list_append.append(5)
print(list_append)

#2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим
# списком [7, 8, 9] за допомогою функції extend()
list_extend = [4, 5, 6]
add = [7, 8, 9]
list_extend.extend(add)
print(list_extend)

#3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()
print(list_extend.index(6))

#4. Визначити довжину списку list_append за допомогою функції len()
print(len(list_append))

#Робота зі словниками:
#1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
# та вивести на екран дані, які знаходяться в ключах car та where
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test.get('car'),'is in', dict_test.get('where'))

#2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення
print(dict_test.keys())
print(dict_test.values())

#3. За допомогою функції items() вивести на екран пари ключ - значення
#print(dict_test.items(), sep='\n')
for x in dict_test.items():
    print(x[0],'>',x[1])