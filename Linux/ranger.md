---
id: ranger
aliases: []
tags: []
---
*Back*
    [[!Lin]]

# Base
---
Источники: [Pikabu - Файловый менеджер *ranger*](https://pikabu.ru/story/faylovyiy_menedzher_ranger_5784003)


## Files
---

| File               | Descript                                                 |
|--------------------|----------------------------------------------------------|
| `rifle.conf`       | Для открытия файлов через  ranger                        |
| `plugins/`         | Плагины,  Py  скрипты                                    |
| `rc.conf`          | команды выполняющиеся при запуске  ranger                |
| `comands.py`       | команды доступные после ввода ":"                        |
| `commands_full.py` | появляется после --copy-config=commands_full             |
| `-`                | Служит в качестве ссылки для пользовательских команд,    |
| `-`                | игнорируется  ranger                                     |
| `colorschemes/`    | цветовые схемы                                           |
| `bookmarks`        | список закладок,                                         |
| `-`                | add bookmarks `m<key>` remove `um<key>`                  |
| `copy_buffer`      | сохр. путей всех скопированных в данный момент файлов    |
| `-`                | команды `:save_copy_buffer` и `:load_copy_buffer`        |
| `history`          | история команд                                           |
| `tagged`           | список помеченных файлов, для дополнения необходимо      |
| `-`                | нажать  t, затем следует назначить имя тега `"<tagname>` |
| `-`                | для удаления  T                                          |

## Key binding
---
### Me binds
---


### Share binds
---
>[!Note] CLI
```sh
:w

:delete                 Удалить
: <standart command>
! <standart command>
,
```

>[!Note] CLI
```sh
/                       # Search
    n                   # Ищет все вхождения
=                       # Chmod
```

>[!Note] CLI
```sh
<return> or l(right)   Открыть файл
```

>[!Note] **z**
```sh
zh                      показывает скрытые файлы
```

>[!Note] **y**
```sh
yy          Yank
    y.      Yank name (whith out extension)
    yn      Name
    yd      Dir
    yp      Puth
    ya      Скопировать mode add
    yr      Скопировать mode remove
    yv      Скопировать mode toggle
```

>[!Note] **p**
```sh
pp          Insert
```
>[!Note] **d**
```sh
dd          Cut
```

>[!Note] **d**
```sh
a       Rename (курсор размещается в конце имени файла, перед разрешением)
A       (Анал.) (после разрешения)
```

> [!NOTE] Tabs
```sh
Ctrl + n # Создать вкладку
Ctrl + v # Закрыть вкладку

# Переход по вкладкам
Tab
Alt + <numb>
gt
```


