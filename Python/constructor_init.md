---
id: constructor_init
aliases: []
tags: []
---
**Back**
    [[!Python]]

# Конструирование и инициализация
---

## New
---
```python
def __new__(cls, [...]):
    pass
```
- Это первый метод, который будет вызван при инициализации объекта. Он принимает в качестве параметров класс и потом любые другие аргументы, который переданы в  `__init__`

*P.S. Хорошо описан в документации*


## Init
---
Инициализатор класса.
 Ему передается все, с чем был вызван первоначальный конструктор.

```python
def __init__(self, [...]):
    pass
```

>[!Example]
```python
class FileObject:
    def __init__(self, filepath='puth/to/file', filename='sample.txt'):
        self.file = open(join(filepath, filename), 'r+')

    def __del__(self):
    self.file.close()
    del self.file
```


## Del (delete)
---
Деструктор объекта.
Всегда вызывается по завершении работы интерпритатора

```python
def __del__(self):
    pass
```

**Деструкторы** вызываются при удалении методов

- В нем указываются действия, которые необходимо выполнить при удалении объекта
    - Н-р: удаление или освобождение ресурсов, которые использовал объект

- Деструктор вызывается автоматически интерпритатором (его явным образом вызывать не требуется)

>[!Example]
```python
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Created Person with name a {self.name}")

    def __del__(self):
        print(f"Deleted Person with name a {self.name}")
tom = Person("Tom") # >> Created Person with name a Tom
                    # >> Deleted Person with name a Tom
```
- Программа создает один объект *Person* и хранит ссылку на него в переменной tom
    - Создание объекта вызовет выполнение **конструктора**.
    - Завершение программы вызовет выполнение **деструктора**
