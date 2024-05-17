class ValueType(Exception):
    pass


def value_type(n):
    if n < 0:
        raise ValueError('n должно быть положительным числом')
    if n == str:
        raise TypeError('n должно относиться к типу "int"')
    return n * 5


try:
    result = value_type(-5)
except ValueError as exc:
    print(f'Ошибка: {exc} n отрицательное число')
    raise
except TypeError as exc:
    print(f'Ошибка:{exc} n другой тип данных')
else:
    print(result, 'Вроде получилось')
