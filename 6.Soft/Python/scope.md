---
id: scope
aliases: []
tags: []
---

**More**
    [[!Python]]

# Область видимости (scope)
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
