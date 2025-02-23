---
id: try_except
aliases: []
tags: []
---
**Back**
    [[!Python]]

## Обработка ошибок и исключений
---
```python
try:
    # Instructions

except [typeError]:
    # Instructions

else:               # (opt)
    # Instructions

finally :           # (opt)
    # Instructions
```
https://docs.python.org/3/library/exceptions.html

>[!Example]
```python
try:
    Весь потенциальный код в котором мб исключение
excect [typeError]:
    Код выполняющийся в случае исключения
else:
    Код выполняющийся в случае если исключение не вызвано
[finally:]
    Выполняется в любом случае
```
- Зачастую блок **finally** используется для освобождения используемых ресурсов, например, для закрытия файлов.

>[!Warning] Ошибки и Исключения
>- Ошибку нельзя обработать, а исключение Py обрабатываются при выполнении программы.
>- Ошибка может указывать на критические проблемы (которые приложение и не должно перехватывать), а исключения - состояния, которые стоит попробовать перехватить.
>- Ошибки - вид непроверяемых и невозвратимых ошибок таких как `OutOfMemoryError`, которые не стоит пытаться обработать.

Обработка искл. делает код более отказоустойчивым и помогает предотвращать потенциальные проблемы, которые могут привести к преждевременной остановке выполнения.

Исключения в *Py* это ошибки, обнаруживаемые при исполнении, но не являющиеся критическими.

**More**

## Виды ошибок
---
- Синтаксические `SyntaxError`
    - Ошибка отступа `IndentationError`
- Недостаточно памяти `OutOfMemoryError`
    - Данную ошибку не рекомендуется обрабатывать
- Ошибки рекурсии 'RecursionError'
- Исключения

| Error             | Description                                        |
| ----------------- | -------------------------------------------------- |
| BaseException     | Б.т. для всех типов исключений                     |
| Exception         | Б.т. применяется для создания своих исключений     |
| AriphmeticError   | Б.т. для искл. связанных с арифм. опер.            |
| ZeroDivision      | Ошибка деления на нуль                             |
| OverFlow          | Ошибка переполнения                                |
| FloatingPoint     | Ошибка плавающей точки                             |
| LookupError       | Б.т. для искл. при не корректном обращении в колл. |
| BufferError       | Невозможность выполнить операцию с буффером        |
| SyntaxError       | Ошибки синтаксиса                                  |
| RuntimeError      | Ошибки выполнения                                  |
| ValueError        | Ошибки типа переменных                             |
| KeyError          |                                                    |
| TypeError         | Ошибка типа данных                                 |
| ZeroDivisionError |                                                    |
| KeyboardInterrupt | Попытка остановить программу `Ctrl+C`              |
| AsswerionError    | Ошибка утверждения                                 |
| AttributeError    | Ошибка атрибута                                    |

# Создание собственных исключений
---
**Raise**  - Оператор для генерации исключений

```python
try:
    age = int(input("Введите возраст: "))
    if age > 110 or age < 1:
        raise Exception("Некорректный возраст")
    print("Ваш возраст:", age)
except ValueError:
    print("Введены некорректные данные")
except Exception as e:
    print(e)
print("Завершение программы")
```
Оператору `raise` передается объект `BaseException` - *в данном случае объект    Exception*.
- В конструктор этого типа можно ему передать сообщение, которое затем можно вывести пользователю.


>[!Example] Пример создания собственного исключения
---
```python
class PersonAgeException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage


    def __str__(self):
        return f"Недопустимое значение: {self.age}. " \
                f"Возраст должен быть в диапазоне от {self.minage} до {self.maxage}"


class Person:
    def __init__(self, name, age):
        self.__name = name
        minage, maxage = 1, 110
        if minage < age < maxage:
            self.__age = age
        else:
            raise PersonAgeException(age, minage, maxage)


    def display_info(self):
        print(f"Name: {self.__name} Age: {self.__age}")


try:
    tom = Person("Tom", 37)
    tom.display_info() # Name: Tom Age: 37

    bob = Person("Bob", -23)
    bob.display_info()
except PersonAgeException as e:
    print(e) # Недопутимое значение: -23. Возраст должен...
```

