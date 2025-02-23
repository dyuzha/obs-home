---
id: class
aliases: []
tags: []
---
**Back**
    [[!Python]]


# Class
---

## Нейминг
---
**Base/Parent/Super** class - родительский класс
**Derived/child/parent** class - подкласс (дочерний)

## @staticmethod
---
```python
class Person:
    __type = "Person"

    @staticmethod
    def print_type():
        print(Person.__type)

Person.print_type()

tom = Person()
tom.print_type()
```
- В данном случае в классе Person определен атрибут класса `__type`, который хранит значение, общее для всего класса - название класса.

- Также в классе Person определен статический метод `print_type`, который выводит на консоль значение атрибута `__type`.
    - Действие этого метода не зависит от конкретного объекта и относится в целом ко всему классу - вне зависимости от объекта на консоль будет выводиться одно и то же значение атрибута `__type`.
    -> Поэтому такой метод можно сделать статическим.

## Классовые методы
---
```python
class MyClass:
    def __init__(self):
        pass


    @classmethod
    def func(cls, arg: str):
        print(arg)


class YouClass(MyClass):
    @classmethod
    def func(cls):
        super().func("Работает также и с классовыми методами")
```
