from functools import singledispatch
from typing import overload

"""
Использование декоратора functools.singledispatch
Ориентирован на тип первого аргумента

Результат функции обязан возвращать туже сигнатуру, что и базовая функция
"""

@singledispatch
def hello() -> None | int:
    raise TypeError('Unsupported type')


# Тоже работает
# @singledispatch
# def hello(_) -> None | int:
#     raise TypeError('Unsupported type')


@hello.register
def _(name: str, age: int) -> None:
    print(f'Hello {name}')
    print(f'Your age is {age}')


@hello.register(int)
def _(age) -> int:
    print(f'Your age is {age}')
    return age


@hello.register
def _(name: str, data: dict):
    print(f'Hello {name}')
    print(f'Твоя информация: {data}')


age = hello(7)
print(f'age: {age}')
print('---')
hello('mat', 3)
print('---')
hello('mat2', {'age': 4, 'sex': 'M'} )



