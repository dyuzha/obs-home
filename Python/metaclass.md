---
id: Classes
aliases: []
tags: []
---
**Back**
    [[!Python]]

# Метаклассы
---
Метакласс - создает объект класс по созданию объектов экземпляров класса

- Обычно это делаетcя для **API**, когда хочется создавать классы в соответствии с текущем контекстом.


## Порядок событий
---
1. Интерпритатор **Py** запускается
2. Интерпритатор **Py** создает **object**  с помощью функции `type()`
3. Класс **tupe** определяется как потомок класса **object**
4. Все остальные классы в *Py* создаются с помощью функции `type()`, которая теперь является потомком класса **object**


## Иерархия объектов
---
- Metaclass (object и class)
    - class (object и class)
        - object (object)


## Type
---
**type()**:
- Функция для создания классов (динамически)
- Функция для определения типа объекта
*Семантика type будет совершенно разной, в зависимости от количесвта передаваемых аргументов (1 или 3)*


### Type в качестве определения объекта
---
`type(obj)` >>> Возвращает тип объекта


### Type в качестве метакласса
---
**type** - Это встроенный метакласс для создания классов в *Py* и не создается никаким другим классом!

`type(name, bases, dict)` >>> Создает тип

**name** - Имя для создаваемого типа,
-> становиться атрибутом `__name__`

**bases** - Кортеж с родительскими классами,
-> становиться атрибутом `__bases__`

**dict** - Словарь, который будет являться пространством имен для тела класса
-> становиться атрибутом `__dict__`

Методы - это атрибуты ссылающиеся на объект функции

>[!Example] Все стандартные типы данных пораждены метаклассом type
```python
>>> type(3) # Целое число порождено классом целых чисел
<class 'int'>

>>> type(int) # Класс целых чисел, порожден метаклассом type
<class 'type'>

>>> type(str)
<class 'type'>

>>> class A: pass # Пользовательские классы также создаются этим метаклассом
>>> type(A)
<class 'type'>

>>> type(type) # И даже метакласс type как бы порождает сам себя
<class 'type'>
```
#### Пример создания простого класса
---
С помощью оператора **class**
```python
>>> class MyClass: pass

>>> MyClass()
<__main__.MyClass object at 0xfffecd02f5f0>
```

C помощью функции **type()**
```python
>>> type('MyClass', (), {})

>>> MyClass()
<__main__.MyClass object at 0xfffecd03fee1>
```

#### Пример создания сложного класса
---
С помощью оператора **class**
```python
class ParentClass():
    pass

class ChildClass(ParentClass):
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old")

# Посмотреть порядок поиска методов и атрибутов
print(ChildClass.__mro__)
# (<class '__main__.ChildClass'>, <class '__main__.ParentClass'>, <class 'object'>)

print(ChildClass.species)
# Homo sapiens

child = ChildClass('James', 13)

child.greet()
# Hello, my name is James and i am 13 years old

print(child.species)
# Homo sapiens
```

C помощью функции **type()**
```python
ParentClass = type('ParentClass', (), {})

def greet(self):
    print(f"Hello, my name is {self.name} and i am {self.age} years old")

ChildClass = type('ChildClass', (ParentClass,), {
    'species': "Homo sapiens",
    '__init__': lambda self, name, age: setattr(self, 'name', name) or
        setattr(self, 'age', age),
    'greet': greet
    })


# Посмотреть порядок поиска методов и атрибутов
print(ChildClass.__mro__)
# (<class '__main__.ChildClass'>, <class '__main__.ParentClass'>, <class 'object'>)

print(ChildClass.species)
# Homo sapiens

child = ChildClass('James', 13)

child.greet()
# Hello, my name is James and i am 13 years old

print(child.species)
# Homo sapiens
```


В данной строчке используется оператор or чтобы выполнилось оба выражения
- Если будет использован оператор and, то выражение вернет True, даже если `age = None`
```python
'__init__': lambda self, name, age: setattr(self, 'name', name) or
    setattr(self, 'age', age),
```

## Методы метаклассов
---

#### new
---
Метод `__new__` метакласса вызывается при создании нового класса.

- Используется для создания нового класса.
- Возвращает новый класс.
- Вызывается перед созданием класса.

Аргументы:
    cls: Сам метакласс
    name: Имя нового класса
    bases: Кортеж бызовых классов
    attrs: Словарь атрибутов нового класса


#### init
---
Метод `__init__` метакласса вызывается после создания новго класса, но для его инициализации.

- Используется для инициализации класса и выполнения любой необходимой настройки для новго класса.
- Конструктор срабатывает, сразу после создания объекта (класса).

Аргументы:
    cls: Сам класс
    name: Имя нового класса
    bases: Кортеж базовых классов нового класса
    attrs: Словарь атрибутов нового класса


## Тривиальные способы содания метаклассов
---
Использовать метод **type** напрямую - неудобно

1. Используя функцию
```python
def my_metaclass(name, bases, attrs):
    print(f"Ctratung class {name}")
    attrs['description'] = 'Default description'
    return type(name, bases, attrs)

class MyClass(metaclass=my_metaclass):
    def my_method(self):
        print("This is the my_method method.")

# Ctratung class MyClass

print(MyClass.description)
# Default description

my = MyClass()
print(my.description)
# Default description

my.my_method()
# This is the my_method method.
```

2. Используя наследования
```python
class MyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creating class {name}")
        attrs['description'] = "Default description"
        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        print(f"Initializing class {name}")

class MyClass(metaclass=MyMetaclass):
    def my_method(self):
        print("This is the my_method method.")

# Creating class MyClass
# Initializing class MyClass

print(MyClass.description)
# Default description

my = MyClass()
print(my.description)
# Default description

my.my_method()
# This is the my_method method.
```

## Кейсы
---

### Добавление наследования при помощи метакласса
---
```python

# Наследование
class DBMeta(type):
    """Базовый Метакласс"""
    def __new__(cls, name, bases, attrs):
        bases = (DeclarativeBase,) + bases
        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls._db_url = ''
        cls._engine = create_engine(cls._db_url, echo=False)
        cls._session = sessionmaker(bind=cls._engine)

```


### Метакласс для автоматического логирования
---
```python
import logging
from functools import wraps

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def log_function_call(func):
    """Декоратор для логирования вызовов функций."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}\n")
        return result
    return wrapper


class LoggingMeta(type):
    """
    Метакласс для автоматического применения декоратора логирования
    ко всем методам класса.
    """
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value):
                attrs[attr_name] = log_function_call(attr_value)
        return super().__new__(cls, name, bases, attrs)


```


### Добавление атрибутов класса
---
```python
class DBMeta(type):
    """Базовый Метакласс"""
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls._db_url = "override_me" # Аттрибут класса
        cls._engine = create_engine(cls._db_url, echo=False) # Аттрибут класса
        cls._session = sessionmaker(bind=cls._engine) # Аттрибут класса
```


sources: [Habr - Метаклассы в Python](https://abr.com/ru/companies/piter/articles/592127)
