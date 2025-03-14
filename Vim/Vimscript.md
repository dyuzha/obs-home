# Base

:echo $MYVIMRC - укажет путь до *vimrc*

>[!Note] Ctrl + ]
> При чтении *help* перемещает по ключевым словам
> *Ctrl + 0 - возращает назад

**echo** - выводи.. ну, понятно...
**echom** - сохраняет сообщение истории сообщений 
    - Удобно для отладки
**mesages** - история сообщений

Конец строки:
`<NL>` - Unix
`<CR>` - Mac

> [!NOTE] Многострочные операторы
> `<cmd> | <cmd_2>`
> на-р:
> `:echom "foo" | echom "bar"`

# Операторы
---


## Операторы ожидания
---

**Оператор** - это команда, которая ожидает введенную команду перемещения, а затем выполняет определенное действие (между тем местом где находится курсор и тем местом куда приводит перемещение) (`y`, `c`, `d`)
на-р:

| key | Operant | Move                                |
|-----|---------|-------------------------------------|
| dw  | Delete  | Until the next word                 |
| ci( | Change  | Insert the brackets (внутри скобок) |
| yt, | Copy    | To the coma (до запятой)            |

- [Создание собственного оператора ожидания](vim-create-operator.md)

*Правила работы оператора ожидания*
- Если сопоставление в ожидании оператора заканчивается визуально выделенным текстом, *vim* будет работать с этим текстом.
- В противнос случае *vim* будет работать с текстом между исходной позицией курсора и новой позицией

>[!Example]
```vim
:onoremap in( :<c-u>normal! f(vi(<cr> " внутри следущих скообок
:onoremap il( :<c-u>normal! F)vi(<cr> " внутри предыдущих скобок
```
- при *cmd* in произойдет `f(vi` - *vim* найдет первую `(` и выделет все ее содержимое
- соответсвенно дальше примениться *операнд ожидания*, на-р `d`/`c`/`y` 


## Операторы перемещения
---
на-р: `j, k, h, l, 0, $ и тд`

`:onoremap <key> <cmd>` - создать новый оператор перемещения
- он будет также работать с операторами ожидания
>[!Example]
`:onoremap p i(` - теперь если поставить курсор внутри скобок и ввести `dp` - vim удалит все что в скобках

*Vim* ожидает опрератора перемещения и видит **p**, в результате он к нему относиться как i(.
- О данной команде можно думать как о "удалить параметры"

`:onoremap ih :<c-u>execute "normal! ?^==\\+$\r:nohlsearch\rkvg_"<cr>`
- редактирукт заголовок *md* (over `=======` при нажатии `cih`) 
`?` - поиск в обратном направленнии
`^==` - для любой строки начинающейся с двух или более знаков '='
`\+$` - заканчивающаяся переносом строки
- Это поставит курсор на первом символе '='
`:nohlsearch` - удаляет выделение из поиска, чтобы он не отвлекал
`kv` - вверх, выделить
`g_` - перейти к последнему не пустому символу в строке
    - он используется вместо $`, т.к. `$` выделяет также символ конца строки (`\n`)

:onoremap ah :<c-u>execute "normal! ?^==\\+$\r:nohlsearch\rg_vk0"<cr>`
- редактирует вокруг заголовка (удаляет head и =====)

Отличия:
(ih) `kvg_` 
(ah) `g_vk0`
`g_v` - перейти к последнему не пустому символу и перекл. в визульный режим
`k` - вверх
`0` - перейти к первому символу в строкео


# Local

>[!Note]
`setlocal <parammetrs>` -  применяет параметр для текущего файла (другие табы трогаться не будут)

>[!Note] 
`:nnoremap <buffer> Q x`
`:nnoremap Q dd`
- В данном случае vim выполнит первую команду для данного буфера, а не вторую, т.к. **вторая команда более специфична**

# Autocommands

`:autocmd BufNewFile * :write`
- при создании нового файла - он автоматически сохраняется
>[!Example]
>`edit foo`
>`:q`
- в итоге файл останется!!!

**Syntax**
`autocmd <ожидаемое событие> <фильтр шаблона> <command>`


# Параметры SET

a) Логические параметры
b) Параметры которые принимают значение

> [!Note] Одновременная настройка нескольких параметров
`set number numberwidth=6`

## Логические параметры

:set [no]number
- Можно инвертирировать параметры, если поставить "!"  в конце них
    :set [no]number!
- Можно узнать у *vim* какой параметр установлен прямо сейчас

:set wrap 
- перенос строки

:set shiftround (set sr) 
    - CTRL-T и CTRL-D ([no]tab for line in insert mode)

:set shiftwidth (set sw)
    - Anal. in normal mode

:set matchtime
- Десятые доли секунды, чтобы показать соответствующую скобку, если установлен параметр showmatch.  Обратите внимание, что это не миллисекунды, как другие параметры, устанавливающие время.  Это должно быть совместимо с Nvi. (:help)

## Параметры со значениями
`:set numberwidth=10`

## `<mode>noremap`
- не рекурсивный анлог `<mode>map`
    - NOREcursion map

# Map (сопаставления)

`:inoremap <esc> <nop>` - отключает клавишу!!!

- **nmap** normal
- **vmap** visual
- **imap** insert

- **map** работает и в visual и в normal (вроде)
`:map <key> <func>`

`:map - x`
- *Биндит* на "-" вырезание 1-го символа 

`:imap <c-d> <esc>ddi`
- `Ctrl - d` удаляет строку в insert mode
- `<esc>` нужно для того чтобы перейти в нормальный режим, после чего выполнить замену
- `i` переводить обратно в режим вставки (если добавит между символами пробел, то он отработает как ПРОБЕЛ, то есть на строку вниз)

`:nunmap <key>` - **Удаление сопоставлений** - в нормальном режиме
:iunmap <key>
:vunmap <key> - ну вы поняли...

## Специальные символы

`:map <space> viw`
- `<space>` выделит все слово

`:map <c-d> dd`
- `<Ctrl + d>` выполнит команду `dd`

`:map <a - d> dd`
- анал. для `<Alt + d>`

## Leader

`:let mapleader = ","`
- Инициализация символа лидер
    - Префиксный ключ для составных команд

`:nnoremap <leader>d dd` - пример использования

### Local leader

`:let maplocalleader = "\\"`
- локальный лидер - префикс для сопастовлений, которые вступают в силу только для определенных типов файлов
- например таких как файлы *Py* или *HTML*-файлы

# abbrev (Сокращения - встроенные сниппеты)  

`iabbrev <pattern> <resume>` 
>[!Example]
```vim
:iabbrev @@ matvey_10@gmail.com
```
- В результате при после написания `@@` не ключевого символа, данный шаблон замениться на `matvey_10@gmail.com`

# FAQ
Источник: [Яндекс Дзен - Изучаем Vimscript](https://dzen.ru/a/Y4-F5wRroy5eNLj6?share_to=link)
