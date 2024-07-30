# Check terminal opt.
---
```sh
stty -a
```

#### Перебиндить клавиши
---
```sh
stty <name> <new-key>
```

`Ctrl-c` - signal SIGINT
Dos/Windows - "Ctrl-z"
- Прерывает работу приложения

`Ctrl-z` - signal SIGTSTP
- Ставит процесс на паузу

`Ctrl-d` - EOF(End Output File)
- Окончание ввода данных

`Ctrl-v` - Ввод сл. символа
- Ввод следующего символа

`Ctrl-l` - "Очищает экран"
- Подобно `cleer & clear`

`Ctrl-r` - History find
- Поиск по истории

**`Alt-_`** - Insert Args
- Вставка аргументов

`Ctrl-o` - Repeat comands from histoy

https://habr.com/ru/companies/lanit/articles/537596/
