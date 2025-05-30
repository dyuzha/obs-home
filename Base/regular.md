---
id: regular
aliases:
  - Base re
tags: []
---
**Back**
    [[!!Base]]

Реализация:
Py: [[regular|Python]]

# Регулярные выражение (Regular expressions)
---
Шаблонные выражения

# Example
---

| Regular           | Смысл                                    |
|-------------------|------------------------------------------|
| `simple text`     | "simple text"                            |
| `\d`              | любая цифра                              |
| `\w`              | любая буква                              |
| `\d{5}`           | Последовательность из 5 цифр             |
| `\d\d/\d\d/\d{4}` | Даты ДД/ММ/ГГГГ (и то что на это похоже) |
| `\b`              | граница слова                            |
| `\b\w{3}\b`       | Слова из 3-ех букв                       |
| `[-+]?\d+`        | Целое число, например, 7, +17, -43, 002  |
| `[-+]?`           | Либо -, либо +, либо пусто               |
| `(.*?)`           | Любой текст                              |

**Проверка пароля**
    `^[z-zA-Z0-9_\-!?]{8,16}$`
**Все числа** *(в том числе и дробные)*
    `\d(\.|.)>\d*`
**Корректный номер телефона**
    `в***ду - загуглишь`


# Якоря
----

| Pattern | Description   | Example                                  |
|---------|---------------|------------------------------------------|
| `^`     | Начало строки | ^Привет -> Найдет Привет в начале строки |
| `$`     | Конец строки  | Пока$ -> Найдет Пока в конце строки      |


 `|` - Или - `Привет | Пока` -> Или Привет или Пока

# Шаблоны соответствующие одному символу

| Pat     | Description                          | Example                        |
|---------|--------------------------------------|--------------------------------|
| `.`     | Любой символ, крому \n               | `м.л.ко` -> мОлОко, малако     |
| `\d`    | Любая цифра                          | `CY\d\d` -> CY33, CY56         |
| `\D`    | Любой симв. кроме цифры              | `123\D123` -> 123_123, 123)123 |
| `\s`    | Space/tab/\n и тд                    |                                |
| `\S`    | not \s                               |                                |
| `\w`    | Любая буква (то что мб частью слова) | `\w\w\w` -> Год, f_3           |
| `\W`    | Не буква, не цифра, не _             | `com\W` -> com!, com?          |
| `\b`    | Начало/конец слова                   |                                |
| `\B`    | Не граница слова                     |                                |
| `[..]`  | Один из симвоолов в скобках          | `[0-9][a-c]` -> 1b, 8c4        |
| `-`     | -                                    | `[_4-]` -> `_`, 4, -           |
| `[^..]` | Любой символ, кроме в скобках        | `<[^>]>` -> `<3>`, `<h>`       |

# Кванитификаторы *(Указание количества повторений)*
---

| Pat      | Description        | Example |
|----------|--------------------|---------|
| `{n}`    | n повторений       |         |
| `{m, n}` | Диапазон от m до n |         |
| `{m,}`   | Не менее m         |         |
| `{, n}`  | Не более n         |         |
| `?`      | Синоним {0,1}      |         |
| `*`      | Синоним {0,}       |         |
| `+`      | Синоним {1,}       |         |

# Спец символы:
---
 `+, *, ?, {, (), \}` - Специальные символы
    - Их необходимо экранировать `\`

# Группы
---

`(http[?s])(://)(a-zA-Z0-8.-_)\.(ru|com)`

- Группы автоматически нумеруются, чтобы можно было посмотреть результат определенной группы
-
    - Группа 0 - `(http[?s])(://)(a-zA-z0-8.-_)\.(ru|com)`
    - Группа 1 - `(http[?s])`
    - Группа 2 - `(://)`
    - Группа 3 - `(a-zA-z0-8.-_)`
    - `\.` - Экранирование точки
    - Группа 4 - `(ru|com)`

`\№` Или `$№` - указание номера группы
    `№` - число или название

# Жадные и ленивые последовательности
---
По умолчанию все последовательности жадные, чтобы их сделать ленивыми,
необходимо добавить знак ?
**ex-l:**
    `(.+)` или `(.*)` - Жадный поиск (до последнего вхождения)
    `(.+?)` или `(.*?)` - Ленивый поиск (до первого вхождения)

**Жадный**
    `<.*>`
    `<a href-"https://yandex.ru">google</a>`
**Ленивый**
    `<.*?>`
    `<a href-"https://yandex.ru">`google</a>

# Опережающие и ретроспективные проверки
---
_Позволяет найти **x** при условии, что за ним идет **y**_

>[!Example]
- Найти все числа после которых идет `$` (цены)
    `\d+(?=\$)`
    Ноутбук за `500`$
        - т.е.  `$` не включен

X(>=Y)  - Найти все X, если за ним следует Y
X(?|)   - Найти все X, если за ним **НЕ** следует Y
(<=Y)X  - Найти X, если перед ним стоит Y
(?<!Y)X - Найти X, если перед ним **НЕ** стоит Y
