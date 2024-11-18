
`strlen("foo")` - Длина строки
`len("foo")` - анал. 
`split("foo bar foot")` - разделение (по умолч. пробел) на список
    - `split("one,too,frie", ",")` - меняем разделитель на `,`
`join (["foo", "bar"], "...")` - соединение (`>> foo...bar`)

>[!Example]
`echo join(split("foo bar"), ";")`
- Сначала `["foo", "bar"]`
- Потом `(в результате foo;bar)`


# Change
---
`trim("text for trim", [mask] ,[dir])` 
    dir:    `0`  - удаляет до и после строки (по умолч.)
            `1`  - удаляет до строки
            `2`  - удаляет после строки

`strtrans()` - делает строку пригодной для печати 
`tolower("Foo")` - lowercase
`toupper("Foo")` - uppercase

# Find
---
gettext() 


Source: [ЯндексДзен - список строковых функций](https://dzen.ru/a/Y73efRa4P0zV57fF?share_to=link)

 
