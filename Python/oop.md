> Back
> [[Python]]

>**More**
>[[magic]]


# ООП простыми словами #
---
**Класс** - Чертеж робота.
**Объект** - Робот.
**Наследование** - Добавление опций к роботу (крыльев, двигателя и тд)
**Полиморфизм** - Общий функционал для всех роботов (не важно как реализован, важно ОДНОИМЕННОСТЬ функций).
**Инкапсуляция** - Броня для робота (*private* и *protected*) - робот полностью защищен от внешних вмешательств.

Когда создается объект, первым делом вызывается метод `__new__` *(а не `__init__`)*


# Type
---
- Альтернативный способ создания классов.
`type` - это class для классов, т.е. **метакласс** (фабрика по созданию классов)

>[!Note] Sample
```python
type(<class-nm>,
    <tuple parents classes>,
    <dictionary {attr:value}>
```

## Добавление метода
---
Для добавления метода необходимо определиться функцию с нужной *сигнатурой* и присвоить ее в качестве атрибута.
>[!Note] Sample
```python
Foo = type('Foo', (), {'bar': True})

def echo_bar(self):
    print self.bar

FooChild = type('FooChild', (Foo), {'echo_bar': echo_bar})
Использование быстрых клавиш в командной строке Linux (BASH)
my_foo = FooChild()
my_foo.echo_bar()

>>> True
```


# Метаклассы
---
**Основная цель метаклассов** - автоматически изменять класс в момент создания.
- Обычно это делаетcя для **API**, когда хочется создавать классы в соответствии с текущем контекстом.

>[!Warning] Алгоритм действий *Py*
```python
class Foo(Bar):
    pass
```
Есть ли у класса **Foo** аттрибут `__metaclass__`?
    Да: Создает в памяти объект-класс с именем Foo, используя то, что указано в `__metaclass__`.
    Нет: *Py* ищет `__metaclass__` в:
            - родительском классе (в данном случае *Bar*)
            - на уровне модуля
        Если не нашел ни одного `__metaclass__`, то использует **type** для созданият объекта-класса.

## Пользовательские **метаклассы**
---
`__metaclass__` мб любым вызываемым объектом - не обязательно формальным классом

[Habr - Метаклассы в Python](https://habr.com/ru/companies/piter/articles/592127/)

# Функция `super()`
---
> [!FAQ] Какой из методов test() будет вызван?
```python
class FirstClass:
	def test(self):
		print("First")

class SecondClass:
	def test(self):
		print("Second")

class ThirdClass(FirstClass, SecondClass):
	def test(self):
		super().test()

t = ThirdClass()

if __name__ == '__main__': t.test()
```

>[!Info] Система наследования в *Py* использует алгоритм поиска "Линеризация C3" Этот алгоритм отпределяет порядок, в котором *Py* будет искать методы при испольщовании функции `super()`
> Порядок определения методов
> - подкласс
> - 1-ый класс в списке наследования (ответ на вопрос выше)
> - 2-ой класс в списке наследования
> - и т.д.
> - вызывается метод из базового класса object

*Источник:* [Letpy.com - super](https://letpy.com/handbook/builtins/super/)

# Функции для оюъектов и классов
---
`vars(obj)` - выводит все аттрибуты объекта в виле словаря
`dir(obg)` - анал. но + методы
`setattr(obj, key, value)` - создает аттрибут 
`getattr(obj)` - 

# Аннотации свойств
---
- *getter* и *setter* называются одинакого!
- *setter* определяется после свойства getter!!! *(property)*
## property (геттер)
---
```python
@property
def age(self):
    return self.__age()
```

## setter
---
```python
@age.setter
def age(self, age):
    if 0 < age < 110:
        self.__age = age
    else:
        raise ValueError("Недопустимое значение age")
```

## deleter

# Наследование
---
**Base/Parent/Super class** - родительский класс
**Derived/child/parent** class - подкласс (дочерний)

```python
def parents_func(self, new_value):
    super().parents_func(self)
    self.new_function = new_value
```

# Class
---
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
    - Действие этого метода не зависит от конкретного объекта и относится в целом ко всему классу - вне зависимости от объекта на консоль будет выводится одно и то же значение атрибута `__type`. 
    \-> Поэтому такой метод можно сделать статическим.




