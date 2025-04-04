---
id: oop
aliases: []
tags: []
---
 **Back**
    [[!Python]]

# ООП простыми словами
---
Объектно Ориентированное Програмиирование

**Класс** - Чертеж робота.
**Объект** - Робот.
**Наследование** - Добавление опций к роботу (крыльев, двигателя и тд)
**Полиморфизм** - Общий функционал для всех роботов (не важно как реализован, важно ОДНОИМЕННОСТЬ функций).
**Инкапсуляция** - Броня для робота (*private* и *protected*) - робот полностью защищен от внешних вмешательств.


### Функции для объектов и классов
---
`vars(obj)` - выводит все аттрибуты объекта в виле словаря
`dir(obj)` - анал. но + методы
`setattr(obj, key, value)` - создает аттрибут
`getattr(obj)` -


## Объект (Object)
---
**Объект** - Это сущность, имеющая:
- состояние (оперделяется его полями - атрибутами)
- поведение (определяется методами)
*Метод это атрибут, ссылающийся на объект функции*

```python
# Посмотреть атрибуты объекта
dir(object)
```

### Под катом
---
Чтобы указатель на участок памяти можно было считать объектом, необходимо 2 поля:
- Счетчик ссылок (Число, показывающее, сколько раз другие объекты ссылаются на данный в коде)
- Тип

```Python
# Создается 3 ссылки на объект, но объект, создается только 1 раз!
>>> a = b = c = object()
```

### Иерархия объектов
---
- Metaclass (object и class)
    - class (object и class)
        - object (object)


### Создание объектов
---
Когда создается объект, первым делом вызывается метод `__new__` *(а не `__init__`)*


### Функция super()
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


### Аннотации свойств
---
- *getter* и *setter* называются одинакого!
- *setter* определяется после свойства getter!!! *(property)*


#### property (геттер)
---
```python
@property
def age(self):
    return self.__age()
```

#### setter
---
```python
@age.setter
def age(self, age):
    if 0 < age < 110:
        self.__age = age
    else:
        raise ValueError("Недопустимое значение age")
```

#### deleter
---

