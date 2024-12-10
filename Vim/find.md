[[Commands.md]]

#Syntax
---
`/<pattern>[/<numb>]` - посик `pattern`
- `<numb>` - порядковый номер вхождения

`/<pattern>/<move>` - поиск `<pattern>`, с последующим переходом на заданное смещение на заданное число количество строк вверх или вниз 
>[!Example]
`/<pattern>/2` - найдет первое вхождение и переместиться на 2 строчки вниз
`/<pattern>/-2` - найдет первое вхождение и переместиться на 2 строчки вверх

`/` - поиск предыдущего шаблона

##### Примеры
---
`\d\d\d\d\([.\/-]\)[01]\?\d\1[0-2]\?\d` - поиск дат (Четыре цифры (год), потом значок . или / или -, потом необязательный 0 или 1, потом цифра (месяц; причем допустимо и 19, мы не гонимся за точностью), потом тот же разделитель, потом еще цифра или две, причем первая меньше 3 (это день).)
`[а-я]\+` - русское слово без `ё`
`[a-z][a-z0-9]*` - идентификатор (буква, потом буквы и цифры) - **(???)**

- see [regular](vim--regular.md)



# Классы символов
---
**Классы символов** задаются в квадратных скобках 
`[eyuioa]` - глассные
**Все символы означают сами себя** 

#### Исключения
---
`^ [] - \` *(некоторые  зависят от позиции в тексте)*

`.` - любой символ кроме конца строки
`..` - любые два символа кроме конца строки

- Можно исользовать дефис (`-`) для создания диапазона
    - поэтому если он нужен, то используется либо первым, либл последним
`[a-z]`
`[0-9]`
`[i-n]`

Если первым символом идет `^` то в класс входят все символы, не перечисленные в скобках.
- Если нужна сама *крышка* (`^`), то ставим ее **не первой**

##### Регистр
---
Если поиск регистронезависимы, то регистр роли не играет
- `\с` - перед классом отключает регистр 

##### Пример регулярных выражений
---
- `[A-z]` - английский алфавит
    - `[A-Za-z]` - тоже самое
- `[А-яЁё]` - русский алфавит 
    - Так как `ё` в символах *ANSII* идет не по порядку, ее необходимо определять отдельно
- `[A-z_0-9.]` - символы идентификаторы в языке R **(???)**



##### POSIX-классы
---
POSIX-классы относится только к ASCII 
- Т.е. к английскому *тексту* или `коду`
- Их необходимо ставить вместе с квадратными скобками (`[]`) внутри класса
>[!Example]
`[[alpha]]`
`[[.6[:upper:]]]` - совпадает с `[A-Z]`, c точкой `.` или `6`
```vim
[:alnum:] " Алфавитно-цифровые символы
[:alpha:] " Буквы
[:blank:] " Пробелы и табуляции
[:cntrl:] " Управляющие символы
[:digit:] " Цифры
[:graph:] " Печатные символы (без пробела)
[:print:] " Печатные символы (c пробелом) 
[:lower:] " Нижний регистр
[:upper:] " Верхний регистр
[:punct:] " Знаки препинания
[:space:] " Невидимые символы
" Отдельные символы
[:tab:]
[:return:]
[:escape:]
[:backspace:]
```

##### Класс с игнорирование акцентов
---
>[!Example]
`[[=a=]]` - *отловит* все это: a, á, à, â, ä


