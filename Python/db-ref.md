Back \=> [[data-base]](data-base.md)

# Data types 
---

| type    | description                                      |
| ------- | ------------------------------------------------ |
| null    | указывает на отсутствие значения                 |
| integer | целое значение (положительное или отрицательное) |
| real    | число с плавающей точкой                         |
| text    | строка                                           |
| blob    | бинарные данные                                  |
| NUMERIC | все 5 типов (любой) ((анал. affinity))           |


# Ограничения
---
## PRIMARY KEY 
```sqlite
id INTEGER PRIMARY KEY
```
- Данное поле будет выступать в качестве первичного ключа

>[!Warning] Установка первичного ключа на уровне таблицы
```sqlite
CREATE TABLE users (
    id INTEGER,
    name TEXT,
    age INTEGER,
    email TEXT,
    PRIMARY KEY(id)
);
```

>[!Warning] Установка составного первичного ключа
```sqlite
CREATE TABLE users (
    id INTEGER,
    name TEXT,
    age INTEGER,
    email TEXT,
    PRIMARY KEY(id, name)
);
```
- Составной первичный ключ

## AUTOINCREMENT
```sqlite
id INTEGER PRIMARY KEY AUTOINCREMENT
```
- Автоматически увеличивает данное число на 1

## UNIQUE 
```sqlite
email TEXT UNIQUE
```
- Данные строки должны быть уникальными

>[!Warning] Определение ограничения на уровне таблицы
```sqlite
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    email TEXT,
    UNIQUE (name, email)
);
```
- В данном случае устанавливается ограничение сразу для двух столбцов

## DEFAULT
```sqlite
age INTEGER DEFAULT 18
```
- Выставляет значение по умолчанию


## NOT / NOT NULL 
```sqlite
name TEXT NOT NULL,
```
- Столбец name не допускает значение NULL

>[!info] По умолчанию любой столбец, если он не представляет первичный ключ,может принимать значение NULL.

## CHECK 
- Создает ограничение для диапазона значений
```sqlite
name TEXT NOT NULL CHECK(name != '')
age INTEGER NOT NULL CHECK(age >0 AND age < 100)
```

>[!Warning] Использование CHECK на уровне таблицы
```sqlite
CREATE TABLE users
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    CHECK ((age >0 AND age < 100) AND (name !=''))
);
```

## CONSTRAINT 
- С помощью данного оператора можно задавать имена ограничениям.
    - Для последующего управления ими.

>[!Example]
```sqlite
CREATE TABLE users
(
    id INTEGER,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    CONSTRAINT users_pk PRIMARY KEY(id),
    CONSTRAINT user_email_uq UNIQUE(email),
    CONSTRAINT user_age_chk CHECK(age >0 AND age < 100)
);
```
# Внешние ключи
---
- Позволяют установить связи между таблицами. Внешний ключ устанавливается для столбцов из зависимой, подчиненной таблицы, и указывает на первичный ключ из связанной таблицы

## Syntax
```python
[CONSTRAINT имя_ограничения] - # имя для ограничения внешнего ключа
FOREIGN KEY (col1, col2, ... colN) 
REFERENCES main_tb (col_main_tb1, col_main_tb2, ... col_main_tbN)
[ON DELETE действие] # задают действие при удалении строки из гл таблицы
[ON UPDATE действие] # задают действие при изменении строки из гл таблицы
```
### ON DELETE/ON UPDATE
- `CASCADE` - автоматически удаляет/изменяет строки из зависимой таблицы при удалении/изменении связной строки
- `SET NULL` - выставляет значение `NULL` при удалении/изменении связной строки
    - В этом случае столбец внешнего ключа должен поддерживать должен поддерживать `NULL`
- `RESTRICT` - отклоняет удаление или изменение строк в главной таблице при наличии связанных строк в зависимой таблице
- `NO ACTION` - анал. `RESTRICT`
- `SET DEFAULT` - при удалении связанной строки из главной таблицы устанавливает для столбца внешнего ключа значение по умолчанию, которое задается с помощью `DEFAULT`

# Операторы
---
## INSERT
>[!Note] Sample
```sqlite
INSERT INTO <table-name> 
    (col1, col2, ..., colN)
VALUES 
    (val1, val2, ..., valN);
```
- Добавление данных в бд
>[!Info] При добавлении данных необязательно указывать значения для всех столбцов!
> - Можно опускать при добавлении такие столбцы, которые поддерживают **NULL** / **default**
> - Можно явным образом для них указывать **NULL** 

>[!Example] Если все значения в таблице поддерживают **NULL** и **Default**, то строку можно добвыить сл. способом.
```sqlite
INSERT INTO <name-tb> DEFAULT VALUES;
```
### Множественное добавление
>[!Example]
```
INSERT INTO 
    users(name, age) 
VALUES
    ('Tom', 16),
    ('Bob', 24),
    ('Sam', 35);
```

## SELECT
```sqlite
SELECT <attr>
FROM 
ORDER BY col1 [ASC | DESC], column2 [ASC | DESC]
WHERE
LIMIT
```

## UPDATE
```sqlite
UPDATE <name-db>
SET <attr>
WHERE
    <attr>
```

## DELETE
```sqlite
DELETE FROM <name-tb>
WHERE <....>
```

## DROP
```sqlite
DROP TABLE IF EXISTS [TABLE-NAME]
```
## ATTACH - прикрепление к *db*
```sqlite
ATTACH DATEBASE 'putch/to/file' AS [alias];
```
- т.е., при обращении к данной *db* нужно будет ссылаться на `alias`
    - `alias.name-tb` - к таблице из прикрепленной *db* необходимо обращаться через точку. (как к методу для объектов)
        `CREATE TABLE alias.name-tb` - создать таблицу в прикрепленной *db* после прикреления

## ALTER
Команда **ALTER** используется чтобы изменять уже созданные таблицы.

### Переименование таблицы
```sqlite
ALTER TABLE <name-tb>
RENAME TO <new-name-tb>;
```
### Добавление столбца
```sqlite
ALTER TABLE <name-tb>
ADD COLUMN <name-col> <ограничения>;
```
### Переименование столбца
```sqlite
ALTER TABLE <name-tb>
RENAME COLUMN <name-col> TO <new-name-col>;
```
### Удаление столбца
```sqlite
ALTER TABLE <name-tb>
DROP COLUMN <name-col>;
```

# Действия с таблицами
---
## Создание таблицы
```sqlite
CREATE TABLE [TABLE-NAME]
```

>[!Note] Sample
```sqlite
CREATE TABLE [TABLE-NAME] (
   [col1] [DATE-TYPE] [ATTR]
   [col2] [DATE-TYPE] [ATTR]
   ...
   [colN] [DATE-TYPE] [ATTR]
);
```

>[!Note] Sample
```sqlite
CREATE TABLE IF NOT EXISTS <table-name> (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
```
- `IF NOT EXISTS` - Проверяет существует такая таблица или нет

## Удаление таблицы
---
```sqlite
DROP TABLE IF EXISTS [TABLE-NAME]
```



