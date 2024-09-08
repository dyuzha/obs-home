# Syntax
---
`autocmd <ожидаемое событие> <фильтр шаблона> <command>`
- В этих командах нельзя использовать спец. символы (такие как `<cr>`)

## Example
---
`:autocmd BufNewFile * :write`
- при создании нового файла - он автоматически сохраняется
>[!Example]
[`edit foo`] [`:q`] - в итоге файл останется!!!
` :autocmd BufNewFile *.txt :write` - Тоже самое что в примере выше,но применятеся только к файлам *txt*

`:autocmd BufWritePre *.html :normal gg=G` - при создании файла *html* и последующем его форматировании - файл автоматически отформатируется до стандартов *HTML*

**Можно несколько несколько событий**
`:autocmd BufWritePre,BufRead *.html :normal gg=G` - тоже самое но и при чтении

`:autocmd BufNewFile,BufRead *.html setlocal nowrap` - Это отключает перенос строк всякий раз, когда вы работаете с HTML-файлом.

`:autocmd FileType python nnoremap <buffer> <localleader>c I#<esc>` 
`:autocmd FileType cpp,javascript nnoremap <buffer> <localleader>c I//<esc>` 
    - комментирует строку в стиле языка

Если в vim добавить несколько одинаковых **autocmd**, то вим их объединенит. 
- Source ~/.vimrc перечитывает весь файл, включая автокоманды которые вы определили. Это означает, что каждый раз когда Vim выполняет source ~/.vimrc вы будете дублировать автокоманды, что приведет к замедлению работы Vim, поскольку он выполняет одни и те же команды снова и снова.
    - Для этого их необходимо добавить в группы и использовать `: autocmd!`
> [!Example] 
```vim
:augroup testgroup
: autocmd BufWrite * :echom "Foo"
: autocmd BufWrite * :echom "Bar"
:augroup END

:augroup testgroup
: autocmd!
: autocmd BufWrite * :echom "Baz"
:augroup END
```
- В таком случае vim перезапишет их

# События
---
## Reading

# Writing
---
- `BufNewFile` - начинаем редактировать файл, который не существует
- `BufReadPre` - начинаем редактировать новый буфер, перед прочтением файла
- `BufRead` - начинаем редактировать новый буфер, после прочтения файла
- `BufReadPost` - начинаем редактировать новый буфер, после прочтения файла
- `BufReadCmd` - перед началом редактирования нового буфера Cmd-событие
- `FileReadPre` - перед чтением файла с помощью команды ":read"
- `FileReadPost` - после чтения файла с помощью команды ":read"
- `FileReadCmd` - перед чтением файла с помощью команды ":read" Cmd-событие
- `FilterReadPre` - перед чтением файла из команды фильтра
- `FilterReadPost` - после чтения файла из команды фильтра
- `StdinReadPre` - перед чтением из stdin в буфер
- `StdinReadPost` -  после считывания из stdin в буфер

# Buffers
- `BufWrite` -начинаем записывать весь буфер в файл
- `BufWritePre` -начинаем записывать весь буфер в файл
    - Применяет команду перед сохранением файла
- `BufWritePost` -после записи всего буфера в файл
- `BufWriteCmd` -перед записью всего буфера в файл Cmd-событие
- 
- `FileWritePre` -запуск записи части буфера в файл
- `FileWritePost` -после записи части буфера в файл
- `FileWriteCmd` -перед записью части буфера в файл Cmd-событие
- 
- `FileAppendPre` -начинаем добавлять в файл
- `FileAppendPost` -после добавления в файл
- `FileAppendCmd` -перед добавлением к файлу Cmd-событие
- 
- `FilterWritePre` -запуск записи файла для команды фильтра или diff
- `FilterWritePost` - после записи файла для команды фильтра или diff

# Options
- `FileType` -когда параметр "тип файла ( filetype )" был установлен
    - применяет команду для определенного типа файла
    - set `filetype?` - посмотреть значений
- `Syntax` -когда параметр "синтаксис ( syntax )" был установлен
- `EncodingChanged` -после того, как параметр "кодировка ( encoding ) " был изменен
- `TermChanged` -после того, как значение 'term' изменилось
- `OptionSet` -после установки любой опции ( option )

# Startup and exit
- `VimEnter` -после выполнения всех работ по запуску
- `GUIEnter` -после успешного запуска графического интерфейса
- `GUIFailed` -после запуска графического интерфейса произошел сбой
- `TermResponse` -после получения ответа терминала на t_RV
- 
- `QuitPre` -при использовании :quit, прежде чем принимать решение о выходе
- `ExitPre` -при использовании команды, которая может привести к выходу Vim
- `VimLeavePre` -перед выходом из Vim, перед записью файла viminfo
- `VimLeave` -перед выходом из Vim, после записи файла viminfo
- 
- `VimSuspend` -при приостановке Vim
- `VimResume` -когда Vim возобновляется после приостановки


# Terminal
 - `TerminalOpen` -после создания терминального буфера
- `TerminalWinOpen` -после создания буфера терминала в новом окне


# Various (разное)
- `FileChangedShell` -Vim замечает, что файл изменился с момента начала редактирования
- `FileChangedShellPost` -После обработки файла, измененного с момента начала редактирования
- `FileChangedRO` -перед внесением первого изменения в файл, доступный только для чтения
- 
- `DiffUpdated` -после того, как различия ( diff ) были обновлены
- `DirChanged` -после того, как рабочий каталог изменился
- 
- `ShellCmdPost` -после выполнения команды оболочки
- `ShellFilterPost` -после фильтрации с помощью командной оболочки
- 
- `CmdUndefined` -используется пользовательская команда, но она не определена
- `FuncUndefined` -используется пользовательская функция, но она не определена
- `SpellFileMissing` -используется файл орфографии ( spell ), но он не может быть найден
- `SourcePre` -перед sourcing Vim-скрипта
- `SourcePost` -после sourcing скрипта Vim
- `SourceCmd` -перед sourcing a Vim script Cmd-event
- 
- `VimResized` -после изменения размера окна Vim
- `FocusGained` -Vim получил фокус ввода
- `FocusLost` -Vim потерял фокус ввода
- `CursorHold` -пользователь некоторое время не нажимает клавишу
- `CursorHoldI` -пользователь некоторое время не нажимает клавишу в “режим вставки" ( insert mode )
- `CursorMoved` -курсор был перемещен в обычном режиме ( Normal mode )
- `CursorMovedI` -курсор был перемещен в режиме вставки ( Insert mode )
- 
- `WinNew` -после создания нового окна
- `TabNew` -после создания новой вкладки
- `WinClosed` -после закрытия окна
- `TabClosed` -после закрытия
- `WinEnter` -после входа в другое окно
- `WinLeave` -прежде чем выйти из окна
- `TabEnter` -после перехода на другую вкладку страницы
- `TabLeave` -прежде чем покинуть страницу с вкладкой
- `CmdwinEnter` -после входа в окно командной строки ( command-line )
- `CmdwinLeave` -перед выходом из окна командной строки ( command-line )
- 
- 
- `CmdlineChanged` -после внесения изменений в командной строке ( command-line )
- `CmdlineEnter` -после того, как курсор переместится в командную строку ( command line )
- `CmdlineLeave` -прежде чем курсор покинет командную строку ( command line )
- 
- `InsertEnter` -запуск режима вставки ( Insert mode )
- `InsertChange` -при вводе <Вставить> (<Insert>) в режиме вставки или замены
- `InsertLeave` -при выходе из режима вставки ( Insert mode )
- `InsertCharPre` -когда символ был набран в режиме вставки ( Insert mode ), перед его вставкой
- 
- `ModeChanged` -после изменения режима
- 
- `TextChanged` -после внесения изменений в текст в обычном режиме ( Normal mode )
- `TextChangedI` -после внесения изменений в текст в режиме вставки ( Insert mode ), когда всплывающее меню не отображается ( popup menu is not visible )
- `TextChangedP` -после внесения изменений в текст в режиме вставки,( Insert mode ) когда всплывающее меню отображается ( popup menu visible )
- `TextYankPost` -после того, как текст был скопирован или удален
- 
- `SafeState` -ничего не ожидает, будет ждать, пока пользователь введет символ
- `SafeStateAgain` -повторное сохранение SafeState
- 
- `ColorSchemePre` -перед загрузкой цветовой схемы ( color scheme )
- `ColorScheme` -после загрузки цветовой схемы ( color scheme )
- 
- `RemoteReply` -был получен ответ от сервера Vim
- 
- `QuickFixCmdPre` -перед выполнением команды быстрого исправления ( quickfix command )
- `QuickFixCmdPost` -после выполнения команды быстрого исправления ( quickfix command )
- 
- `SessionLoadPost` -после загрузки файла сеанса ( session file )
- 
- `MenuPopup` -непосредственно перед отображением всплывающего меню ( popup menu )
- `CompleteChanged` -после завершения режима вставки ( Insert mode ) меню изменилось
- `CompleteDonePre` -после завершения режима вставки,( Insert mode ) перед очисткой информации ( clearing info )
- `CompleteDone` -после завершения режима вставки,( Insert mode ) после очисткой информации ( clearing info )
- 
- 
- `User` -должен использоваться в сочетании с ":doautocmd"
- `SigUSR1` -после обнаружения сигнала SIGUSR1

