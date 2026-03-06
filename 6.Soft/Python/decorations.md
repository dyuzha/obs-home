---
id: decorations
aliases:
  - Decorations
tags: []
---

# Decorations
---
Декоратор без functools
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hi, {name}")
```
При таком методе, метаданные оригинальной функции (н-р, ее имя и docstring) заменяются метаданными wrapper функции

Декоратор с functools
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper
```

Теперь если проверить `say_hello.__name__` или `say_hello.__doc__`, мы увидим оригинальные значения, а не данные wrapper-функции.

