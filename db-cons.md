---
tags: []
---
# Init #
---
```sh
sqlite3
```
- Запустить консоль **sqlite**

```sqlite
.open [db-name]
```
- Открыть файл бд

```sqlite
.help
```
- Вывести справку


# Mode
---
Изменение выходных параметров
```sqlite
.mode
```
Возможные варианты:
- ascii
- box
- csv
- column
- html
- insert
- json
- line
- list
- markdown
- quote
- table
- tabs
- tcl

# INSERT #
---
В режиме вставки вывод отформатирован для сходства с операторами INSERT SQL.
- Данный режим можно использовать для генерации текста, который может позже можно применить в качестве входных параметров для другой *db*.

>[!Example]
```sqlite
.mode insert new-tb
SELECT * FROM name-tb;
INSERT INTO "new-tb"
VALUES('hello',10);
INSERT INTO "name-tb"
VALUES('bye',20);
```
- При определении режима вставки необходимо дать дополнительный аргумент, который является названием таблицы...
- Другие режимы вывода включают "html", "json" и "tcl".

# .output #
---
>[!Example]
```sqlite
.output <name-file>
```

# .once #

>[!Example]
```sqlite
.once '|open -f'
```
- Позволяет наблюдать за выводом в текстовом редакторе
---
