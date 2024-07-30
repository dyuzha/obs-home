# Fast Begin
---
```python
import sqlite3
```

```python
connection = sqlite3.connect('my_databse.db')
```
- Устанавливаем соединение с бд
* В контексте работы с *db* в *Python*, когда устанавливается соединение с *db* - создается объект соединения.

```python
cursor = connection.cursor()
```
- Создает объект **cursor** для выполнения *SQL*-запросов и операций с *db*.
- *Cursor* - Это механизм, который позволяет отправлять *SQL*-запросы *db* и получать результаты запросов.
> [!TIP] *Представляет соединение в качестве объекта.*

```python
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')
```
- Создаем таблицу Users

```python
connection.commit()
connectiom.close()
```
- Сохраняем изменения и закрываем таблицу





# cursor #
---
*Курсор* - это механизм, который позволяет отправлять *SQL*-запросы *db* и получать результаты этих запросов. 
- Предоставляет методы для выполнения *SQL*-запросов и получения результатов. 

## Metods ##
---

### Для получения запросов ###
---
```python
execute('<SQL-reqest ?>', (<values>))
```

```python
executemany()
```

>[!Example]
```sqlite
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
```


### Для получения результатов ###
---
```python
fetchone()
```
- Итератор

```python
fetchall()
```
- Список строк
