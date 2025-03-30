---
id: datetime
aliases: []
tags: []
---
**Back**
    [[!Python]]

**More**
    [[timeago]]

# Datetime
---
```python
import datetime
```
Модуль для работы со временем в Python

Весь функционал сосредочен в виде следующих классов:
- date
- time
- datetime

## Date
---
```python
# Создание (использование конструктора)
date(year, month, day)
# Например
yesterday = datetime.date(2025, 5, 2)
print(yesterday) # 2025-05-02

# Получение сегодняшней даты
today = date.today()
print(today) # 2025-05-03
# Форматирование вывода
print("{}.{}.{}".format(today.day, today.month, today.year))
```


## Time
---
```python
# Создание
time([hour] [, min] [, sec] [, microsec])
# Все  параметры необязвтельные, и если какой-то параметр пропустить, он будет инициализирован нулем
```

## Datetime
---
```python
# Создание
datetime(year, month, day, [, hour] [, min] [, sec] [, microsec])

# Текущее дата, время
now = datetime.now()
print(now) # 2017-05-03 11:18:56.239443

print("{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute))  # 3.5.2017  11:21

print(now.date())
print(now.time())
```


## More
---
```python
time.clock()
# - в Unix, возвращает текущее время
# - в Windows, возвращает время, прошедшее с момента первого вызова данной функции

# Преобразует время, выраженное в секундах с начала эпохи в строку вида:
# "Thu Sep 27 16:42:37 2012"
time.ctime() # [секунды]

# Преобразует время, выраженное в секнудах с начала эпохи
# в struct_time (где DST флаг == 0)
time.gmtime() # [секунды]

# Приостонавливает выполнение программы на заданное кол-во секунд
time.sleep() # [секунды]
```

