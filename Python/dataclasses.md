---
id: dataclasses
aliases:
  - dataclass
tags: []
---

# dataclasses
---
Призваны для автоматизации генерации кода классов, которые используются для хранения данных


## Примеры
---
>[ !example ] Пример класса без использования данного модуля
```python
class RegularBook:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

    def __eq__(self):
        """Необходимо переопределить данный метод"""
        pass

    def __repr__(self):
        """Необходимо переопределить данный метод"""
        pass
```

>[ !example ] Пример класса с испрользованием декоратора
```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str = "Unknown"
```
Aнотации типо - обязательны
    Можно указать `Any` из модуля `Typing`

На выходе получается класс с реализованными методами
- `__init__`
- `__repr__`
- `__str__`
- `__eq__`

Так как это обычный класс, от него можно наследоваться и создавать произвольные методы


## Неизменяемый класс
---
>[ !example ] Неизменяемый класс
```python
@dataclass(frozen=True)
class UnFlexible:
    pass
```


## Изменяемые значения по умолчанию
---
```python
@dataclass
class Bookshelf:
    books: List[Book] = []
```
Интерпретатор сообщит об ошибке:
`ValueError: mutable default <class 'list'> for field books is not allowed: use default_factory`

Для избежания проблем, предлагается использовать параметр `default_factory` функции `field`

```python
@dataclass
class Bookshelf:
    books: list = field(default_factory=list)
```


Sourses:
    [Habr - Dataclasses](https://habr.com/ru/articles/415829/)
    [StackOverFlow](https://stackoverflow.com/questions/53632152/why-cant-dataclasses-have-mutable-defaults-in-their-class-attributes-declaratio)
