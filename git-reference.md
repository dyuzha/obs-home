---
tags:
  - git
---

# Init #
---
```
git init  
```

```
git add <file(s)> - добавляет файл(ы) под версионный контроль (начинает их отслеживать)
```

```
git clone <url> - Клонирует репозиторий
```

```
git status - Определяет состояния файлов
```
- -s (--short) - Сжатый вывод status

```
git commit - Фиксирует добавляя коментарий
```
- -m \<text for commit> - Добавляет комментарий в ''
- -v Добавляет к комментарию в vim (для напоминания) вывод diff
- -a Индексирует все отслеживаемые файлы (минует команду add)

# Diff #
---
```
git diff - Расширенный вариант команды 'status'
```
- --staged / --cashed - Сравнивает проиндексированные изменения с последним коммитом

```
git difftool - Посмотреть вывод diff сторонними командами
```
- --tool-helper - Показывает список установленных программ

# Remove #

```
git rm - Удаляет файл из рабочего каталога и из отслеживаемых в git
```
- -f - На случай, если файл изменен и проиндексирован 
- --cashed \<file(s)> - Удаляет файл из индекса, но оставляет в рабочем каталоге.

```
git mv <file> <file2>- Перемещение / переименование
```

# Логи #
---

```
git log - Выводит историю коммитов
```
- --graph - Выводит коммиты в виде графа
>[!Example]
>```
>$ git log --pretty=format:"%h %s" --graph
>* 2d3acf9 Ignore errors from SIGCHLD on trap
>* 5e3ee11 Merge branch 'master' of git://github.com/dustin/grit
>|\
>| * 420eac9 Add method for getting the current branch
>* | 30e367c Timeout code and tests
>* | 5a09431 Add timeout protection to grit
>* | e1193f8 Support for heads with slashes in them
>|/
>* d6016bc Require time for xmlschema
>* 11d191e Merge branch 'defunkt' into local

- -p (--path) - Показывает разницу, внесенную в каждый коммит
- -2 - Ограничивает вывод до 2-ух записей
- --stat - Показывает статистику измененных файлов для каждого коммита 
- ---shortstat - -Отображает только строку с количеством изменений/вставок/удалений для команды --stat
- --name-only - Показывает список измененных файлов после информации о коммите
- --name-status - Показывает список файлов, которые:
    - добавлены
    - изменены
    - удалены
--abbrev-commit - Показывает несколько символов SHA-1 чек-суммы вместо 40
--relative-date   
--oneline - Cокращение для --pretty=oneline --abbrev-commit
--since=2.weeks
- --pretty=oneline - Выводит каждый коммит в одну строчку
          =short
          =full
          =fuller
          =format - Позволяет указать формат для вывода опций.

>[!Example]
>```
$ git log --pretty=format:"%h - %an, %ar : %s"
ca82a6d - Scott Chacon, 6 years ago : Change version number
085bb3b - Scott Chacon, 6 years ago : Remove unnecessary test
a11bef0 - Scott Chacon, 6 years ago : Initial commit 
 


### Опции для `git log --pretty=format` ###
---

| Опция |     Описание вывода      |
| ----- | :----------------------- |
| %H    |      hash  commits       |
| %h    |      reduction hash      |
| %T    |       tree's hash        |
| %t    |  reduction tree's hash   |
| %P    |      parent's hash       |
| %p    | reduction parent's hash  |
| %an   |      author's name       |
| %ae   |      author's email      |
| %ad   |      author's date       |
| %ar   |  relative author's date  |
| %cn   |     commiter's name      |
| %ce   |   commiter's email by    |
| %cd   |     commiter's date      |
| %cr   | commiter's relative date |
| %s    |         content          |


# Remote #
---

```
git remote - Выводит список удаленных репозиториев
```
**origin** - имя по умолчанию, которое *Git* дает серверу, с которого производилось клонированиеnm
    - -v Выводит адреса для чтения и записи

```
git remote add <shortname> <url> - Добавляет удаленный репозиторий
```

```
git fetch - Получает данные из удаленной ветки, но не сливает их ни с чем!!
```

```
git pull - Автоматически получает изменения из удаленной ветки и сливает их со своей
```

```
git push <remote-name> <branch-name> - Отправляет ветку на сервер
```

```
git remote show <branch-name> - Показывает информацию об удаленном репозитории 
```
- Показывает какая именно ветка отправится на удаленный сервер при *git push*


```
git remote rename <curent_name> <new_name - Переименование удаленного репозитория
```
- ==fail==
```
git remote rm <name> - Удаляет удаленный репозиторий
```
- Или можно написать remove 
- При удалении ссылки на удаленный репозиторий все отслеживаемые ветки и настройки, связанные с этим репозиторием, так же будут удалены
