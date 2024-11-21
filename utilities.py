def calculate_average(numbers):
    if len(numbers) == 0:
        print('Список пустой')
    else:
        result = sum(numbers) / len(numbers)
        return result

def find_max(numbers):
    if len(numbers) == 0:
        print('Список пустой')
    else:
        result = max(numbers)
        return result