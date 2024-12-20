[[Commands.md]]

# grep
---

`grep -R {pattern}` - рекурсивный поиск `pattern` в текущем ниже каталогах. 
`grep -R <cword>` - анал. но слова под курсором

Типы `grep` в *Vim*: 
- Внутренний
- Внешний

## Внутренний grep
---
- `vimgrep` или `vim`

>[!FAQ]
`vim[grep] /pattern/flag path`
- `pattern` - шаблон поиска *(можно использовать регулярные выражения)*
- `flag` - флаг, который можно передать в шаблон поиска
- `path` - аргумент файла *(можно передать несколько аргкментов)*

>[!Example]
`vim word *` - Поиск по всем файлам
`vim wor[dk] *` - Поиск по всем файлам `word` или `work`

`vim word **` - Рекурсивный поиск (по всем файлам и каталогам)
`vim word ../include/**/*.h`
`vim /<pattern>/ **{sh,rb}` -Поиск `<pattern>`, только внутри файлов `.sh` или `.rb`
`vim /<pattern>/ **sh **rb` - анал. выше
`vim /<pattern>/ **/определенный_каталог/**` - Поиск в определенном каталоге
`vim /<pattern>/ puth/to/file1 /puth/to/dir2** *.json bin/**/*sh` - Поиск <pattern> внутри файла `puth/to/file1` и `.json`-файл внутри каталога `/puth/to/dir2` и `.sh`-файла, где-то внутри `bin/` каталога.

- Что бы искать в каталоге отличного от `pwd`, необходимо сначала туда перейти
    `:cd /нужный/каталог`
    `:vim /ну а дальше как всегда`
    - После, *лучше* вернуться обратно *(при помощи `cd`)*

- Также можно взаимодействовать с некоторыми внешними командами:
    - на-р: `find` или `git`
    ```vim
    :vim /<pattern>/g `find . -type f -name 'docker*'
    :vim /<pattern>/g `git ls-files --modified` " man git-ls-files
```
### Поиск файлов в Arglist
---
`vim /echo/g ##`


### Флаги
--
- `g` - Позволяет считать несколько совпадений <pattern> за одно
- `fg` - Нечеткий поиск по всем строкам (на предмет строк, похожих на`<pattern>`) 
- Флаг (который идет после других) - `%` - для поиска в тек. буфере


**Поиск слова под курсором**
- Сначала нажать `*` - для выделения слова под кусрором
- Потом `:vimgrep // *.cpp` - Пустой шаблон для его поиска

- Это `grep` реализованный внутри *Vim*:
    - Он проще, но медленней (т.к. загружает всю информацию в память)

## Внешний grep
---
- Это *Vim*, вызывающий `grep` командной строки *в дочернем процессе оболочки*
- *Vim* вызывает то, что ему передадут, анализирует это и заполняет им окно `Quickfix` 
- При вызове `grep` *Vim* автоматически переходит к первому совпадению
    `grep!` - этого не делает!

>[!Example]
`:grep word *` - Поиск по всем файлам каталога `pwd`
`:grep -R Word *` - Рекурсивный поиск

# Quickfix
---
- По мере выполнения новых поисков `grep`, новые окна `Quickfix`, а последнее отображается внизу
`:copen` - Open *Quickfix* window
`:cclose` - Close the *Quickfix* window
`:cnext` - Go to the next location
`:cprevious` - Go to the previous location
