---
id: ref
aliases: []
tags: []
---

> *Back*
> [[Python]]


# Обработка ошибок и исключений
---
**try**:
    Instructions
**except** \[typeError]:
    Instructions
 else:
    Instructions
**finally** :           # *(opt)*
    Instructions

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
>- Ошибка м. указывать на критические проблемы (которые приложение и не должно перехватывать), а исключения - состояния, которые стоит попробовать перехватить.
>- Ошибки - вид непроверяемых и невозвратимых ошибок таких как `OutOfMemoryError`, которые не стоит пытаться обработать.

Обработка искл. делает код более отказоустойчивым и помогает предотвращать потенциальные проблемы, которые могут привести к преждевременной остановке выполнения.

Исключения в *Py* это ошибки, обнаруживаемые при исполнении, но не являющиеся критическими.

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



# Область видимости / scope
---
Область видимости (scope) определяет *контекст* переменной, в рамках которого ее можно использовать. В *Py* есть два типа контекста:
- Глобальный
- Локальный

>[!example] global
```python
global <var>
```
- Определяет глобальную переменную

>[!example] nonlocal
```python
def outer():
    n = 5
    print(f'outer n = {n}')

    def inner():
        nonlocal n
        n = 25
        print('called nonlocal n')
        print(f'inner n =  {n}')

    inner()
    print(f'outer n = {n}')


outer()             # outer n = 5
                    # called nonlocal n
                    # inner n = 25
                    # outer n = 25
```
- `nonlocal` прикрепляет идентификатор к переменной из ближайшего внешнего контекста (за исключением глобального контекста)
- Обычно `nonlocal` применяется во вложенных функциях, когда надо прикрепить идентификатор за переменной или параметром окружающей внешней функции.


# Функция как тип
---
В *Py* функции фактически представляют отдельный тип. \=> можно присвоить переменной какую-нибудь функцию.
>[!Example]
```python
def say_hello(): print ('Hello')
def say_bye(): print('Bye')

mess = say_hello
mess()                  #Hello
mess = say_bye
mess()                  #Bye
```

# Функция как параметр
---
>[!Example]
```python
def do_oper(a, b, oper):
    res = oper(a, b)
    print(f'result = {res}')

def sum(a, b): return a + b
def mult(a, b): return a * b

do_oper(5, 4, sum)      # result = 9
do_oper(5, 4, mult)     # result = 20
```

# Функция как результат функции
---
Например функция, котороя в зависимости от значения параметра возвращает ту или иную операцию.
>[!Example]
```python
def sum(a, b): return a + b
def sub(a, b): return a - b
def mult(a, b): return a * b

def select_oper(choice):
if choise == 1:
    return sum
elif choise == 2:
    return sub
else:
    return mult


oper = select_oper(1)       # oper = sum
print(oper(10, 6))          # 16

oper = select_oper(2)       # oper = sub
print(oper(10, 6))          # 4

oper = select_oper(3)       # oper = mult
print(oper(10, 6))          # 60
```


# lambda #
---
```python
lambda [par]: инструкция
```

base:
```python
mess = lambda: print("hello")
mess()                      # hello

squar = lambda n: n * n
print(sqare(4))             # 16
```

>[!Example]
```python
def select_oper(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b

oper = select_oper(1)       # oper = sum
print(oper(10, 6))          # 16

oper = select_oper(2)       # oper = sub
print(oper(10, 6))          # 4

oper = select_oper(3)       # oper = mult
print(oper(10, 6))          # 60
```


# Closure / Замыкание #
---
- Функция, которая запоминает свое лексическое окружение даже в том случае, когда она выполняется вне своей области видимости.

3 компонента замыкания:
- Внешняя функция, которая определяет некоторую область видимости и в которой определены некоторые переменные и параметры - лексическое окружение.
- Переменные и параметры (лексическое окружение), которые определены во внешней функции.
- Вложенная функция, которая использует переменные и параметры внешней функции.

>[!Example]
```python
def outer():
    n = 5

    def inner():
        nonlocal n
        n += 1
        print(n)

    return inner
fn = outer()
fn()                                    # 6
fn()                                    # 7
fn()                                    # 8
fn_2 = outer()
fn_2()                                  # 6
fn_2()                                  # 7
fn()                                    # 9
```
- Переменные **fn** и **fn_2** предстваляют собой замыкание, т.к. объединяют в себе 2 вещи: **Функцию** и **Окружение**.
>[!Example] С использованием параметров.
```python
def mult(n):
    def inner(m): return n * m

    return inner

money_for_day = 10

money_for_days = mult(money_for_day)

print(money_for_days(5))                # 50
print(money_for_days(6))                # 60
print(money_for_days(3))                # 30
```

>[!Example] С использованием *lambda*
```python
def mult(n): return lambda m: n * m
```

# Декораторы
---
**Декораторы** в *Py* представляют функцию, которая в качестве параметра получает функцию, и в качестве результата возвращает функцию.
- Декораторы позволяют модифицировать выполняемую функцию, значения ее параметров и ее результат без изменения исходного кода этой функции.

>[!Example]
```python
def select(input_func):
    def output_func():
    ptint("*****")
    input_func()
    ptint("*****")

@select
def hello():
    print("Hello")

hello()                     # *****
                            # Hello
                            # *****
```

#### Определение *функции* в декораторе
---
```python
def check(input_func):
    def output_func(*args):
        input_func(*args)
    return output_func

@check
def print_person(name, age):
    print(f"Name: {name} Age: {age}")

print_person("Tom", 38)
```

>[!Example] Выполнение проверки аргументов с помощью декоратора
```python
def check(input_func):
    def output_func(*args):
        name = args[0]
        age = args[1]
        if age <= 0: age = 1
        input_func(name, age)
    return output_func

@check
def print_person(name, age):
    print(f"Name: {name} Age: {age}")

print_person("Tom", -5)         # Name: Tom, Age: 1
```

>[!Example] Выполнение проверки результата с помощью декоратора
```python
def check(input_func):
    def output_func(*args):
        res = input_func(*args)
        if res < 0: res = 0
        return res
    return output_func

@check
def sum(a, b):
    return a + b

res1 = sum(10, 20)
print(res1)                     # 30

res2 = sum(10, -20)
print(res2)                     # 0
```

# Работа с файлами
---
>[!Example]
```python
f = open('file-nm', '<mode>', encoding='кодировка') # opt: mode = rt

# или так
with open('file.txt', 'r+', encoding='utf-8') as f:
    pass
```

| Mode | Description                                          |
|------|------------------------------------------------------|
| r    | Reed (opt)                                           |
| w    | Wright                                               |
| x    | Wright, if the file do is not exist called exception |
| a    | Anal '>>' in unix                                    |
| b    | Open in blob mode                                    |
| t    | Open in text mode (opt)                              |
| +    | Read and Wright                                      |

# Raise
---
- Оператор для генерации исключений
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

## Создание собственного исключения
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

# Списковые включения

```py
[expression for elem in sequence if condition]

# Example:
even_numbs = [x for x in range(1, 11) if x % 2 == 0]
# [2, 4, 6, 8, 10]
```

# args и kwargs
---
```python
# Используется для передачи неограниченного количесвта
*args # позиционных аргументов
**kwargs # Именованных аргументов
```
