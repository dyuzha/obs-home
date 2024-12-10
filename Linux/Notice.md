# Standart
---
```bash
-a 			# Вывести все объекты.
-c 			# Произвести подсчёт.
-d 			# Указать директорию.
-e 			# Развернуть объект.
-f 			# Указать файл, из которого нужно прочитать данные.
-h 			# Вывести справку по команде.
-i 			# Игнорировать регистр символов.
-l 			# Выполнить полноформатный вывод данных.
-n 			# Использовать неинтерактивный (пакетный) режим.
-o 			# Позволяет указать файл, в который нужно перенаправить вывод.
-q 			# Выполнить скрипт в quiet-режиме.
-r 			# Обрабатывать папки и файлы рекурсивно.
-s 			# Выполнить скрипт в silent-режиме.
-v 			# Выполнить многословный вывод.
-x 			# Исключить объект.
-y 			# Ответить «yes» на все вопросы.
```

# BackUp
```bash
# сделает точную копию раздела sda на разделе sdb.
dd if=/dev/sda of=/dev/sdb bs=64k 

# затрёт содержимое указанного носителя нулями, чтобы информацию было невозможно восстановить.
dd if=/dev/zero of=/dev/sdX 

# сделает загрузочный носитель из скачанного вами образа с дистрибутивом.
dd if=~/Downloads/ubuntu.iso of=/dev/sdX bs=4M 
```

# Bind (X)
```
xmodmap -e "remove Lock = Caps_Lock"; xmodmap -e "keycode 66 = Escape NoSymbol Escape"
```

# Program

```bash
# запрещает удалять файл
chattr +i <file_name>
# снимает запрет
chattr -i <file_name>
```

```bash
# Найти все жесткие ссылки
find . -some <file_name>
# Найти все мягкие ссылки
find . -lname "fie_name"
```

**pling.com** - кастом сайт

```bash
makepkg -isc # Разрешение зависимостей
/sys/class/backlight/intel_backlight/
```
