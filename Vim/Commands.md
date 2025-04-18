# Commands
---

## More
---
[[match.md]]
[[make.md]]
[[grep.md]]
[[find.md]]
[[arglist.md]]

[[map.md]]

[[autocmd.md]]

**Создание собственного оператора**
[[create-operator.md]]

## Visualmode()
---
- Возвращает односимвольную строку, предстваляющую последний тип используемого визуального режима (`v`, `V`, `Ctrl-v`)


### `<c-u>`
---
- Если выделить текст, а после нажать `:`
    - Командная строка автоматически заполниться `'<,'>` (то есть как-бы заполниться выделенным текстом)

- Оператор `<c-u>` - очищает строку *(удалить от курсора до начала строки)*

## normal
---
- `normal` - эта команда которая принимает набор символов и выполняет их как если бы они были введены в обычном режиме. 
- `normal!` - не учитывает сопоставляения (как `nnoremap` для `nmap`) 
>[!Example]
```vim
normal! gg " перемещает в начало файла
normal! >> " tab
```
`normal!` - не распознает специальные символы (наподобие `<cr>`) - есть несколько способов это обойти
    - `execute` - самый простой

## ececute
---
`:execute` - эта команда принимает строку *Vimscript* и выполняет ее как команду
- Просматривает строку на выполнение, которую вы ей указали, перед запуском `execute` заменяет все спец. символы.
>[!Example]
```vim
execute "write" "= :write<cr>
execute "normal! gg" "=gg
```

### Позволяет создавать команды из произвольных строк
---
> [!Example]
```vim
" Vim создает команду путем объединения `rightbelow vsplit ` с резутльтатом вывода `bufname("#")`
:execute "rightbelow vsplit " . bufname("#")
" bufname("#") - возвращает путь к предыдущему буферу.

" объединяет 3 маленьких строчки прежде чем отправить их в однуfr
:execute "normal! gg" . '/for .\+ in .\+:' . "\<cr>"
```
> [!Example]
```vim
:onoremap ih :<c-u>execute "normal! ?^==\\+$\r:nohlsearch\rkvg_"<cr>
" В данном случае `\r` это *escape-последовательность*, которая  означает *возврат каретки*. 
"- `\\` также является *escape-последовательностью*, которая помещает `\` в строку

"Если выполнить данное сопоставление в примере выше, получим сл. результат
:onoremap ih :<c-u>execute "normal! ?^==\+$<cr>:nohlsearch\rkvg_"
"Фактически это возвраты каретки, а не *четыре символа*
"Т.е.
" \\ = \
" \r = <cr>
```


## Varible
---

###### Init
---
```vim
:let <item> = <value>
:let foo = "bar"
:echo foo
```

## Parametrs
---

###### Init
---
```vim
set <item> = <value>
" &value - означает: "ссылайся не на имя, а на *значение*"
```

> [!Example]
```vim
:set textwidth=80
:echo &textwidth
" Логические параметры
:set wrap
:echo &wrap " >> 1
```
> [!Warning] Параметры в качестве переменных
```vim
:let &texteidth = 100
:set textwidth? " >> Vimtexteidth=100
:let &texteidth = &texteidth + 10
:set textwidth? " >> Vimtexteidth=110
```
- Если устанавливать параметры в качестве переменных, раскрывается вся мощь *vim*

### Prefix
---
> [!FAQ] Переменная начатая с `<simbol:>` описывает переменную с огранниченной областью видимости
> `b:` -  в одном буффере
> `w:` -  в одном окне
> `t:` - в одной вкладке
> `g:` - глобальная
> `l:` - внутри функции *(локальная переменная)*
> `s:` - внутри исходного кода *(скрипта vim)*
> `a:` - аргумент функции *(обратиться к аргументам функции можно только через этот префикс)*
> `v:` - управляется редактором *(тоже глобальная переменая)*


## Local
---
```vim
"Установка локального значения вместо глобального
:let &l:<item> = <value>
"на-р:
:let &l:number = 1 " переменная измениться только для текущего буфера
```

## Регистры как переменные
---
```vim
:let @a = "hello!"

" Чтение регистров
:echo @a " >> hello!

" Если выделить тест и скопировть, а после ввести:
:echo @" " >> [скопированный текст]

"Если выполнить поиск /[слово]
:echo @/ " >> слово
" Данный способ позволяет читать и изменить текущий шаблон
```
