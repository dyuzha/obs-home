---
id: ref
aliases: []
tags: []
---
**Back**
    [[!Python]]

## Списковые включения
---
Укороченный способ создания итерируемых объектов

```python
[expression for elem in sequence if condition]

# Example:
even_numbs = [x for x in range(1, 11) if x % 2 == 0]
# [2, 4, 6, 8, 10]
```

## args и kwargs
---
```python
# Используется для передачи неограниченного количесвта
*args # позиционных аргументов
**kwargs # Именованных аргументов
```

## Итератор
---
- Это объект, реализующий в себе интерфейс перебора чего-либо.
(Он содержит правило перебора)

Цикл `for` в действительности взаимодействует не с самой коллекцией, а с итератором объекта коллекции
- Он неявно вызывает функцию `iter`
    `iter(obj)`

**Обход через цикл For**
```python
tumb = ["ножницы", "карандаш", "яблоко", "книга"]
for item in tumb:
    print(item)
```

**Через цикл while**
```python
tumb = ["ножницы", "карандаш", "яблоко", "книга"]
iterator = iter(tumb)

try:
    while True:
        next_val = next(iterator)
        print("Очередное значение:", next_val)
except StopIteration:
    print("Stop iteration")
print("Stop program")
```
Пример создания собственного итератора [[iter]]

## Преобразование в будевое значение
---
```python
def find_user(name):
    users = {"Alice": 25, "Bob":30}
    # Возвращает возраст или None
    return users.get(name)

# 1. Пример использования
age = find_user("Alice")
if age:
    print("Age:", age)
# Сработает, даже если age = 0, т.к. 0 - ложно
else:
    print("User not found")


# 2. Пример использования
age = find_user("Alice")
# Четко проверяем, что результат не None
if age is not None:
    print("Age:", age)
# Если age = 0, не сработает!!
else:
    print("User not found")


def has_user(name):
    users = {"Alice": 25, "Bob":30}
    # Возвращает True, если пользователь найден
    # и False, елси не найден
    return users.get(name) is not None
```
