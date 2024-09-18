# Dict (словари)
---
- `{key:value, key:value}`
    `:echo {'a': 1, 100 = 'foo'}` >> {'a': 1, 100 = 'foo'}
    `:echo {'a': 1, 100 = 'foo',}` >> {'a': 1, 100 = 'foo'}

## Иднексирование
- `{key:value, key:value}[<index>]`
    `:echo {'a': 1, 100 = 'foo',}['a']` >> 1
    `:echo {'a': 1, 100 = 'foo',}[100]` >> foo - перед выполнением поиска, *Vim* приведет индекс к строке

    - Точечный поиск в стиле *Js*
        `:echo {'a': 1, 100 = 'foo',}.a'` >> 1
        `:echo {'a': 1, 100 = 'foo',}.100` >> foo

## Функции
---
- `has_key({dict}, value)` - Присутсвует ли данный ключ в словаре
    `:echom has_key({'a': 100}, 'a')` >> 1
    `:echom has_key({'a': 100}, 'b')` >> 0

- `items({dir})` (упорядоченность не гарантирована)
    `:echom ({'a': 100, 'b': 200})` >> [['a', 100], ['b', 200]]

- `keys({dir})`
- `values({dir})`



# Массивы
---
## Списки
---
- упорядоченные, разнотипные наборы элементов
    `['foo', 3, ['bar', 4]]`

- Индексирование (как в *Py*)
    `:echo [0, [1, 3]][1]` >> [1, 2]
    `:echo [0, [1, 3]][-2]` >> 0

- Разделение (срезы)
    `:echo ['a', 'b', 'c', 'd', 'e'][0:2]` >> ['a', 'b', 'c']
    `:echo ['a', 'b', 'c', 'd', 'e'][-2:-1]` >> ['d', 'e']

    - Можно выходить за пределы списка
        `:echo ['a', 'b'][0:1000]` >> ['a', 'b']

    - Можно опустить первый/последний индекс
        `:echo ['a', 'b', 'c', 'd', 'e'][:1]` >> ['a', 'b']
        `:echo ['a', 'b', 'c', 'd', 'e'][3:]` >> ['d', 'e']
        
## Конкатенация
---
- Нужно использовать `+`
    `:echo ['a', 'b'] + ['c']` >> ['a', 'b', 'c']

## Функции
---
- `add(<var>, 'b')` >> [<var>, 'b']
    ```vim
    let foo = ['a']
    call add(foo, 'b')
    echo foo " >> ['a', 'b']
    ```
- `len(foo)` >> 2

- `get({list}, {index}, {default})` *(default - значение по умолч.)*
    `:echo get(foo, 0, 'lol')` >> a
    `echo get(foo, 100, 'lol')` >> lol

- `index({list}, {value})` - Если *func* не находит `value`, то возвращает -1    
    `index(foo, 'b')` >> 1
    `index(foo, 'nope')` >> -1

- `join({list}, {seperator})` *(если разделитель не указан используется пробел)*
    `join(foo)` >> a b
    `join(foo, '---')` >> a---b
    `join([1, 2, 3], '')` >> 1233

- `reverst(list)`
    ```vim
    :call reverse(foo)
    :echo foo " >> ['b', 'a']
    :call reverse(foo)
    :echo foo " >> ['a', 'b']
    ```

# Function
---
>[!Warning] Функции *vimscript* должны начинаться с загавной буквы, если они не являются частью другой функции
> Большинство программистов везде используют заглавные буквы

>[!Example]
```vim
:function GetMeow()
:	return "Meow string!"
:endfunction

:function Meow()
:	echom "Meow"
:endfunction

:echo(m) Meow() >> "Meow"
:echo(m) GetMeow() >> "Meow string!"
:call Meow() >> "Meow"
tcall GetMeow() >>
```

- При вызове `call` возвращаемое значение отбрасывается *мб полезно, если функция имеет побочные эффекты 
- При вызове `echo(m)`, фунция отрабатывает, а потом выводит возвращаемое значение, если функция не возвращает ничего, то она выводит `0`

>[!Example]
```vim
function TextwidthIsTooWide()
 	if &l:textwidth ># 80
	return	1
	endif
endfunction

set textwidth=100
if TextwidthIsTooWide()
	echom "WARNING: Wide text!"
endif
```

# Varible
---
>[!Example]
```vim
function Varg(...) " Функция может принимать любое кол-во переменных
	echom a:0 " >> 2 (кол-во аргуметов входящие в ...)
	echom a:1 " >> a (первый аргумент функции)
	echom a:000 " >> [`a`, `b`] - список аргументов ... (по идеи echom не может исп-ся с echoM)
endfunction

call Varg("a", "b")
```
>[!Example]
```vim
function Varg(foo, ...)
	echom a:foo
	echom a:0
	echom a:1
	echom a:000
endfunction 
call Varg("hello", "b", "c")
```
>[!Example]
```vim
function Assign(foo)
	let a:foo = "Пустышка"
	echom a:foo
endfunction
call Assign("lll")
```
- Vim выдаст ошибку, так как мы не можем переопределить переменную аргумента

>[!Example]
```vim 
function AssignGood(foo)
	let foo_tmp = a:foo
	let foo_tmp = "yee"
	echom foo_tmp
endfunction
call AssignGood("text")
```
# Number
---
В вим 2 типа числовых переменных
- Целые числа со знаком (32 разрядные)
- Float

>[!Example]
```vim
echom 100 " >> 100
echom 0xff " >> 255 
echom 0Xff " >> 255
echom 010 " >> 8
echom 017 " >> 15
echom 019 " >> 19 так как `9` нет в 8-ой системе счисления
echo 100.1 ">> 100.1
echo 5.45e+4 " >> 5450.0
echo 5.45e4 " >> 5450.0
echo 15.45e-2 " >> 0.1545
echo 5e10 " Error (нет .<numb>)
```
- prefix `0x` или `0X` означает число в 16-ной системе счисления
- prefix `0` - восьмеричное число

## Действия
---
`echo 2 * 2.0 ` >> 4.0
`echo 3 / 2` >> 1
`echo 3 / 2.0` >> 1.5

# String
---
`echom "Hi"` >> Hi

## Конкатенация `.` и приведение типов
---
`echom "hi" + ", " + "world"` >> 0 
`echom "3 мыша" + "2 кота"` >> 5
`echom 10 + "10.10"` >> 20
- Оператор "vim" предназначен только для чисел, в итоге при передаче *строки* оператору `+` *Vim* автоматически переводит строку в `целочисленное` значение

`echom "hi" . ", " . "world"` >> hi, world
`echom 10 . "foo"` >> 10foo
`echom 10.1 . "foo"` >> Error (vim не дает использовать float в качестве строки при конкатенации)

`:echom "foo \"bar\""` >> foo "bar"
`:echom "foo \\bar"` >> foo \bar
- `\` - экранирует символы 

`echo "foo\nbar"` >> foo<return>bar
`echom "foo\nbar"` >> foo^@bar (^@ - символ новой строки)
- `\n` - new line
- `\b` - backspace
- `\r` - return
- `\t` - tab
- см. `:help expr-quote`
 
`echom '\n\\'` >> \n\\ *(литеральная строка)*
`echom 'That''s enough'` >> That's enough (`'` Экранирует саму себя)

## Индексирование
---
- Как и списки 

## Срезы
---
- Как и списки, но
- **Нельзя использовать отрицательные голые индексы со строками**
    `:echo "abcd"[-1] . "abcd"[-2:]` >> cd

## Функции
---
[строковые функции](vim-string-func.md)


# Операторы сравнения
---
`>, <,`
`==` - поведение зависит от настроек пользователя
`==?` - независит от настроек пользователя
`==#` - чувствителен к регистру оператора сравнения


     | operation             | ignorecase | match case | ignore case |
     |-----------------------|------------|------------|-------------|
     | equal                 | '=='       | '==#'      | '==?'       |
     | not equal             | '!='       | '!=#'      | '!=?'       |
     | greater than          | '>'        | '>#'       | '>?'        |
     | greater than or equal | '>='       | '>=#'      | '>=?'       |
     | smaller than          | '<'        | '<#'       | '<?'        |
     | smaller than or equal | '<='       | '<=#'      | '<=?'       |
     | regexp matches        | '=~'       | '=~#'      | '=~?'       |
     | regexp doesn't match  | '!~'       | '!~#'      | '!~?'       |
     | same instance         | 'is'       | 'is#'      | 'is?'       |
     | different instance    | 'isnot'    | 'isnot#'   | 'isnot?'    |

# Условные операторы
---

>[!Example]
```vim
:if 1
:   echom "ONE"
:endif " >> ONE, т.к. 1 = True 
```

>[!FAQ]Строки начинающиеся с числа принудительно преобразовываются в число, в противном случае это 0
`:echom "hi" + 10` >> 10
`:echom "20hi" + 10` >> 20
`:echom "hi20" + 10` >> 10

>[!Example]
```vim
:if 0
:   echom "if"
:elseif "no"
:echom "elseif"
:else
: echom "yes"
:endif
```
- *vim* обработает локальные условия, так как предыдущие были ложными

# Cicle (Циклы)
---

## For
---
```vim
let c = 0
for i in [1, 2, 3, 4]
    let c += i
endfor
echom c " >> 10 (результат 1+2+3+4)
```

## While
---
```vim
let c = 1
let total = 0
while c <= 4
    let total += c
    ler c += 1
endwhile
echom total
```




