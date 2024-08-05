Back \=> [[data-base]]

# Fast Begin
---
## 1. Создание таблицы
---
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

## 2. Удаление таблицы
---
```sqlite
DROP TABLE IF EXISTS [TABLE-NAME]
```

## Прикрепление **DB**
---

```sqlite
ATTACH DATEBASE 'putch/to/file' AS [alias];
```


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


# Ограничения #
---
#### PRIMARY KEY ####
---
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

#### AUTOINCREMENT ####
---
```sqlite
id INTEGER PRIMARY KEY AUTOINCREMENT
```
- Автоматически увеличивает данное число на 1

#### UNIQUE ####
---
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

#### DEFAULT ####
---
```sqlite
age INTEGER DEFAULT 18
```
- Выставляет значение по умолчанию


#### NOT / NOT NULL ####
---
```sqlite
name TEXT NOT NULL,
```
- Столбец name не допускает значение NULL

>[!info] По умолчанию любой столбец, если он не представляет первичный ключ,может принимать значение NULL.

#### CHECK ####
---
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

#### CONSTRAINT ####
---
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

# INSERT #
---
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


## Множественное добавление ##
---
>[!Example]
```
INSERT INTO 
    users(name, age) 
VALUES
    ('Tom', 16),
    ('Bob', 24),
    ('Sam', 35);
```


# SELECT #
---

```sqlite
SELECT <attr>
FROM 
ORDER BY
WHERE
LIMIT
```

# UPDATE #
---

```sqlite
UPDATE <name-db>
SET <attr>
WHERE
    <attr>
```

# DELETE  #
---
```sqlite
DROP TABLE IF EXISTS [TABLE-NAME]
```



# ATTACH #
---

```sqlite
ATTACH DATEBASE 'putch/to/file' AS [alias];
```
- Прикрепоение *db*


# ALTER #
---
Команда **ALTER** используется чтобы изменять уже созданные таблицы.

```sqlite
ALTER TABLE <name-tb>
RENAME TO <new-name-tb>;
```
- Переименование таблицы

```sqlite
ALTER TABLE <name-tb>
ADD COLUMN <name-col> <ограничения>;
```
- Добавление столбца

```sqlite
ALTER TABLE <name-tb>
RENAME COLUMN <name-col> TO <new-name-col>;
```
- Переименование столбца

```sqlite
ALTER TABLE <name-tb>
DROP COLUMN <name-col>;
```
- Удаление столбца

