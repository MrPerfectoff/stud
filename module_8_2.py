def personal_sum(*numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
        return incorrect_data, result

def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError('В numbers записан некорректный тип данных')
        if isinstance(numbers, str):
            numbers = list(numbers)
        total, incorrect_data = personal_sum(numbers)
        count = len(numbers) - incorrect_data
        if count == 0:
            return 0
        return total / count

    except TypeError as exc:
        print(str(exc))
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать