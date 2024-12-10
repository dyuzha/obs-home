source: [dmosk - Работа с пользователями в Linux](https://www.dmosk.ru/miniinstruktions.php?mini=linux-users&ysclid=m3il1ipgox493856692)

# Admin-commands

## Less
- Можно cat
  `less /etc/passwd`

-Получиь строку из файла `/etc/passwd`
  `getent passwd <username>` 
  `>>> username:x:UserID:GroupID::/home/dir:/command/shell`
example:
  `>>> username:x:1001:1001::/home/username:/bin/sh` 

Проверить существование и посмотреть его идентинтификатор
- `id <username>`


## Create
- `useradd` 
Создание пользователя
  `useradd <username> [opt]`
  `passwd <username>`
*Opt:*
  - b --base-dir
  - c --comment (любая текстовая строка)
    - зачастую имя и фамилия

  - g - основная группа
  - G - дополнительная группа
  - k -   

В файле `/etc/default/useradd` есть переменная `$HOME` 
  - В ней указан каталог home по умолчанию (`\home`)

## Eddit
- `usermod` 

## Delete
- `userdel` 

# Chmod
---

command | description                                      |
--------|--------------------------------------------------|
u+x     | разрешить выполнение для владельца               |
ugo+x   | разрешить выполнение для всех                    |
ug+w    | разрешить запись для владельца и группы          |
o-x     | запретить выполнение для остальных пользователей |
ugo+rwx | разрешить все для всех                           |

|Owner           | Groups | Other    |
|----------------|--------|----------|
|User (Владелец) | Группa | Остальные|

`-` - запрещение
`+` - разрешение
`=` - присваивание

примеры
```bash
chmod g+w file
chmod a-wx file
chmod go=rw
```

# About

```bash
# Посмотреть версию
cat /etc/*release 

# Посмотреть проц
lscpu

# Посмотреть оперативку
lsmem

# Посмотреть имя хоста
hostnamectl

# Посмотреть релиз
lsb_release

# Выставить красивую иконку хоста
$ hostnamectl --pretty set-hostname "$(perl -CO -le 'print "\x{1f389}"')"
$ hostnamectl --pretty status
🎉

# Задать имя хосту
hostnamectl set-hostname

# По умолчанию все переносные носители монируются (Astra)
/run/user/1000/media
```
