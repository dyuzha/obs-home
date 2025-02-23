---
id: sqlite
aliases: []
tags: []
---
**Back**
    [[!Python]]

# SQLite
---
```python
import sqlite3
cursor = connection.cursor()
connection = sqlite3.connect('my_databse.db')
```
Устанавливаем соединение с бд
- В контексте работы с *db* в *Python*, когда устанавливается соединение с *db* - создается объект соединения.

Создает объект **cursor** для выполнения *SQL*-запросов и операций с *db*.
- *Cursor* - Это механизм, который позволяет отправлять *SQL*-запросы *db* и получать результаты запросов.
- *Представляет соединение в качестве объекта.*


# Create table
---
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


# Connect
---

## Methods
---
`connect.autocommit`
3 вида:
- False: sqlite3 гарантирует, что транзакция всегда открыта (по умолчанию)
    `connect.commit()` - для закрытия транзакции
    `connect.rollback()` - откатывает изменения до последнего `connect.commit`

- True: sqlite3 испольщует автоматические методы фиксации
    `connect.commit()` - не действует
    `connect.rollback()` - не действует

- LEGACY_TRANSACTION_CONTROL - управление транзакциями до версии 3.12

`connect.isolation_level`
- Управляет устаревшим режимом обработкаи транзакций sqlite3

`connect.in_transaction`
- Возвращает *True*, если транзакция активна и *False* в противном случае

`connect.cursor(factory=Cursor)`
- Метод получения курсора

`connect.blobopen(table, column, row, /,\*, readonly=False, name="main")`
- Метод открывает файлоподобный объект *Blob*, для существующего **SQL-BLOB**
    - `table (str)` - имя таблицы, в которой находиться бинарный объект
    - `column (str)` - имя столбца, в которой находиться бинарный объект
    - `row (str)` - имя строки, в которой находиться бинарный объект
    - `reafonly=False (bool)` - значение *True*, если бинарный объект должен быть открыт без разрешений на запись. (по умолч. False)
    - `name="main" (str)` - имя базы данных, в которой находиться двоичный объект. (по умолч. 'main')

`connect.close` - закрывает соединение с *db*

`connect.create_function(name, num_params, func, *, deterministic=False)`
- Создает пользовательскую функцию, которую позже можно использовать из опереторов *SQL* под именем функции
    - `num_params` - это число параметров (`num_params = -1` - func принимает неограниченное количество параметров)
    - `func` - это вызывамый объект *Py* (функция), которая будет вызываться как функция *SQL*
    - `deterministic = True` - помечается как detetministrc, что позволяет SQL-lite выпронять дополнительныю оптимизацию
>[!Example]
```python
import sqlite3
import hashlib

def md5sum(t):
return hashlib.md5(t).hexfigest()

conn = sqlite3.connect(":memory:")
conn.create_function("md5", 1, md5sum)
cur = conn.cursor()
cur.execute("select md5(?)", (b"foo",))
print(cur.fetchone()[0])

conn.close()
```


## Cursor
---
*Курсор* - это механизм, который позволяет отправлять *SQL*-запросы *db* и получать результаты этих запросов.
- Предоставляет методы для выполнения *SQL*-запросов и получения результатов.

## Methods
---

### Для составления запросов
---
Классическое составления запроса (по порядку - ?, ()) (в разброс - :key, {})
     `cursor.execute('SQL-reqest <?>', (<values>))`
     `cursor.execute('SQL-reqest :<key>', {<key>: <values>})`

Чтобы выполнить запросы из файла:
    ```python
    cursor.executescript("""
        'SQL-reqest <?>'
        'SQL-reqest <?>'
    """)
    ```

- `cursor.executemany('SQL-reqest <?>'), <list>`
    ```python
    purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                 ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                 ('2006-04-06', 'SELL', 'IBM', 500, 53.00)]
    cursor.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
    ```


### Для получения результатов
---
- Выдает по 1 (как итератор) (если нечего выдавать, то возвращает `None`)
    `cursor.fetchone()`

- Возвращает оставшиейся строки
    `cursor.fetchall()` - возвращает пустой список, когда нет достпуных строк

- Извлекает следующий набор строк результата запроса, в виде списка
    - Возращает пустой список, когда нет доступных строк
        `cursor.fetchmany(size=cursor.arraysize)` - (по умолчанию)

- Итератор (в виде курсора)
    ```python
    for row in cursor.execute('SQL-reqest'):
        print(row)
    ```

### More
---
Закрыть курсор сейчас *(а не всякий раз, после вызова `__del__`)*
    `cursor.close()`
    - С этого момента *курсор* станет непригодным для использования. Возникнет исключение **ProgrammingError** (если с закрытым *cursor* курсором предпримут какие-либо операции )

Возвращает идентификатор последней измененной строки в *db* (при испоользовании `INSERT` или `REPLACE`, в инном случае он равен `None`)
    `cursor.lastrowid`

    `cursor.rowcount`

Управляет количеством строк, возвращаемых методом `cursor.fetchmany()`
    `cursor.arraysize`

Предоставляет имена столбцов последнего запроса
- также возвращает кортеж из 7 элементов каждого столбца (где последние 6 элементов каждого столбца равны `None`)
- устанавливается для оператора `SELECT` для соответствующих строк.
    `cursor.description`

Source: [tic](https://docs-python.ru/standart-library/modul-sqlite3-python/obekt-connection-modulja-sqlite3/)




# Поддерживаемые конструкции
---
## try-except-else
---
>[!Example]
```python
try:
    cursor.execute(sql_statement)
    result = cursor.fetchall()
except sqlite3.DatabaseError as err:
    print("Error: ", err)
else:
    conn.commit()
```
## with
>[!Example] Пример из документации (вроде)
```python
with psycopg2.connect("dbname='habr'") as conn:
    with conn.cursor() as cur:
```
