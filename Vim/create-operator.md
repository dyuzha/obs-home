[[Vim/Reference|Reference]]
# Begin
---
Source: [ЯндексДзен Оператор grep часть 1](https://dzen.ru/a/Y8w0G4I4dBVUnjG4?share_to=link)

Target: Создать сопоставленик для поиска слова под курсором 

`nnoremap <leader>g :grep -R word .<cr>` - рекурсивный поиск `grep` 

`nnoremap <leader>g :grep -R <cword> .<cr>`
- `<cword>` - слово под курсором (see :h <cword>)
- `<cWORD>` - учет спец символов
- Это будет ломать `foo;ls`, `ls` - отработает как команда

`nnoremap <leader>g :grep -R '<cWORD>'.<cr>` 
- одинарные ковычки говорят обрабатывать буквально
    - Это будет ломать `that's` (see `:help shellescape()` `:help escape()`)
    -  Что бы это исправить мы заключаем `<cWORD>` в `''`
 
`:nnoremap <leader>g :execute "grep -R '<cWORD>' ."<cr>`
- Это не будет работать, если слово под курсором - `that's`, т.к там есть `'`
    - Что бы это обойти, мы используем `shellescape()`
    - т.к. `shellescape()`, работает со строками, их необходимо динамически создать при помощи `execute`

`:nnoremap <leader>g :execute "grep -R '<cWORD>' ."<cr>`
- В данный момент `.` не корректно отрабатыывает, так как `execute` воспринимает ее как *конкатенацию*
`:nnoremap <leader>g :execute "grep -R " . shellescape("<cWORD>") . " ."<cr>`

- Выполним сл. чтобы проверить:
    - `:echom shellescape("<cWORD>")` >> '<cWORD>', так как `''` - являются часью строки

- Теперб необходимо расширить '<cWORD>', чтобы превратить в фактическую строку, прежде чем передать ее `shellescape()`
    - `:echom expand("<cWORD>")` - выведет слово под курсором, в виде строки *Vim*

- Если вернуть `shellescape()` *Vim* правильно экранирует строку под курсором
    - `:echom shellescape(expand("<cWORD>"))` >> 'that'\''s'

`:nnoremap <leaderg> :exe "grep - R " . shellescape(expand("<cWORD>")) . " ."<cr>`
- Теперь поиск идет как надо  (`:exe[cute]`)

- Теперь заменим `grep` на `grep!`, чтобы не переходить к первому совпадению
- `:oprn<cr>` - добавим в конце строки, чтобы автоматически открывать *Quickfix*

`:nnoremap <leader>g :execute "grep! -R " . shellescape(expand("<cWORD>")) . " ."<cr>:copen<cr>`

# Часть 2
---



