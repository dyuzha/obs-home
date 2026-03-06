---
id: overloard
aliases:
  - overloard
  - Overloard
tags: []
---

# Overloard
---
Перегрузка функции
Это концепция, которая позволяет определять несколько функций или методов с одинаковым именем, но с разными сигнатурами:
- количесвто аргументов
- тип аргументов
- порядок аргументов

Компилятор или интерпретптор выбрирает подходяющую версию функции на основе переданных аргументов. Это используется в строго типизированных языках, чтобы писать гибкий и читаемый код проще.

## Python - варианты реализации
---
Так как, Py язык c динамической типизацией, единственная "актуальная" сигнатура функции доступна только в рантайме.

Встроенная возможность перегрузить функцию
```python
def hello(name_or_age: str | int):
    if isinstance(name_or_age, str):
        print(f'Hello {name_or_age}')
        return
    print(f'Your age is {name_or_age}')

# Или

def hello(name_or_age):
    if isinstance(name_or_age, str):
        print(f"Hello {name_or_age}")
    elif isinstance(name_or_age, int):
        print(f"Your age is {name_or_age}")
    else:
        raise TypeError("Expected str or int")
```

```python
from functools import singledispatch
from typing import NoReturn

"""
Использование декоратора functools.singledispatch

Результат функции обязан возвращать туже сигнатуру, что и базовая функция
"""

@singledispatch
def hello(_) -> None | int:
    raise TypeError('Unsupported type')

# Можно так
@hello.register
def _(name: str) -> None:
    print(f'Hello {name}')

# Или так
@hello.register(int)
def _(age) -> int:
    print(f'Your age is {age}')
    return age
```


