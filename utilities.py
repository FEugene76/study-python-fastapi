def calculate_average(numbers):
    #numbers = [1, 2, 3, 4, 5]  # Пример списка чисел
    if len(numbers) == 0:
        print('Список пустой')
    else:
        result = sum(numbers) / len(numbers)
        return result
        #print('Среднее арифметическое числа из списка:', average)

def find_max(numbers):
    #numbers = [1, 2, 3, 4, 5]  # Пример списка чисел
    if len(numbers) == 0:
        print('Список пустой')
    else:
        result = max(numbers)
        return result
        #print('Максимальное число в списке:', max_number)
