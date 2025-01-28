---
id: Reference
aliases: []
tags: []
---

**Back**
	[[Git]]

# Init
---
``` bash
# Создать ветку с именем 'master' (default)
git init
	# Данный параметр переопределит default branch name
	git config --global init.defultBranch main

# добавляет файл(ы) под версионный контроль (начинает их отслеживать)
git add <file(s)>

# Клонирует репозиторий
git clone <url>

# Определяет состояния файлов
git status

# Сжатый вывод status
- -s (--short)

git commit - Фиксирует добавляя коментарий
	-m <text for commit> # Добавляет комментарий в ''
	-v # Добавляет к комментарию в vim (для напоминания) вывод diff
	-a # Индексирует все отслеживаемые файлы (минует команду add)
```

# Status
---

| Символ | отредактированные           |
| ------ | --------------------------- |
| M      | отредактированные           |
| MM     | 9ask9                       |
| ??     | Новые, неотсеживаемые       |
| A      | Добавленные и отслеживаемые |


# Diff #
---
```bash
git diff # Расширенный вариант команды 'status'
	--staged / --cashed # Сравнивает проиндексированные изменения с последним коммитом

git difftool # Посмотреть вывод diff сторонними командами
	--tool-helper # Показывает список установленных программ

```
# Remove #
---
*Для того чтобы удалить файл из **Git**, его необходимо удалить из отслеживаемых файлов (точнее удалить из индекса) а затем выполнить коммит.*
- В качестве параметров можно передавать:
	- Файлы
	- Каталоги
	- Шаблоны
``` bash
# Удаляет файл из рабочего каталога и из отслеживаемых в git
git rm
	-f # На случай, если файл изменен и проиндексирован
	--cashed <file(s)> # Удаляет файл из индекса, но оставляет в рабочем каталоге.

git mv <file> <file2> # Перемещение / переименование
```

# Logs
---
``` bash
git log # Выводит историю коммитов
	--graph # Выводит коммиты в виде графа
```

>[!Example]
```bash
git log --pretty=format:"%h %s" --graph
	* 2d3acf9 Ignore errors from SIGCHLD on trap
	* 5e3ee11 Merge branch 'master' of git://github.com/dustin/grit
	|\
	| * 420eac9 Add method for getting the current branch
	* | 30e367c Timeout code and tests
	* | 5a09431 Add timeout protection to grit
	* | e1193f8 Support for heads with slashes in them
	|/
	* d6016bc Require time for xmlschema
	* 11d191e Merge branch 'defunkt' into local
```

>[!Note] Флаги для `git log`
```bash
	-p (--path)

	# Ограничивает вывод до 2-ух записей
	-2

	# Показывает статистику измененных файлов для каждого коммита
	--stat

	# Отображает только строку с количеством изменений/вставок/удалений для команды --stat
	--shortstat

	# Показывает список измененных файлов после информации о коммите
	--name-only

	# Показывает список файлов, которые: добавлены, изменены, удалены
	--name-status

	# Показывает несколько символов SHA-1 чек-суммы вместо 40
	--abbrev-commit
	--relative-date

	# Cокращение для --pretty=oneline --abbrev-commit
	--oneline
	--since=2.weeks

	# Выводит каждый коммит в одну строчку
	--pretty=oneline
          =short
          =full
          =fuller
          =format # Позволяет указать формат для вывода опций.

```

```bash
$ git log --pretty=format:"%h - %an, %ar : %s"
ca82a6d - Scott Chacon, 6 years ago : Change version number
085bb3b - Scott Chacon, 6 years ago : Remove unnecessary test
a11bef0 - Scott Chacon, 6 years ago : Initial commit
```

> [!Note] Опции для `git log --pretty=format`

| Опция  |     Описание вывода      |
| ------ | :----------------------- |
| %H     |      hash  commits       |
| %h     |      reduction hash      |
| %T     |       tree's hash        |
| %t     |  reduction tree's hash   |
| %P     |      parent's hash       |
| %p     | reduction parent's hash  |
| %an    |      author's name       |
| %ae    |      author's email      |
| %ad    |      author's date       |
| %ar    |  relative author's date  |
| %cn    |     commiter's name      |
| %ce    |   commiter's email by    |
| %cd    |     commiter's date      |
| %cr    | commiter's relative date |
| %s<br> |         content          |

# Remote #
---
```bash
# Выводит список удаленных репозиториев
# 'origin' - имя по умолчанию, которое Git дает серверу, с которого производилось клонированиеnm
git remote
	-v # Выводит адреса для чтения и записи

# Добавляет удаленный репозиторий
git remote add <shortname> <url>

# Получает данные из удаленной ветки, но не сливает их ни с чем!!
git fetch

# Автоматически получает изменения из удаленной ветки и сливает их со своей
git pull

# Отправляет ветку на сервер
git push <remote-name> <branch-name>

# Показывает информацию об удаленном репозитории
# Можно увидеть какая ветка отправится на удаленный репозиторий при git push
git remote show <branch-name>

# Переименование удаленного репозитория
git remote rename <curent_name> <new_name

# Удаляет удаленный репозиторий
git remote rm <name>
	# Или можно написать remove
	# При удалении ссылки на удаленный репозиторий все отслеживаемые ветки и настройки, связанные с этим репозиторием, так же будут удалены
```

# .gitignore
---
>[!Warning] Правила к шаблонам в *.gitignore*
> - Пустые строки, а также строки начинающиеся с '#' - игнорируются.
> - Стандартные шаблоны являются глобальными и применяются рекурсивно для всего дерева каталогов.
> - Чтобы избежать рекурсии - используйте '/' в начале шаблона.
> - Чтобы исключить каталог добавьте / в конец шаблона.
> - Можно инвертировать шаблон, используя '!' в качестве первого символа.

> [!example] .gitignore
```bash
# Игнорировать все файлы заканчивающиеся на o или на a
*.[oa]
# Игнорировать все файлы заканчивающиеся на тильду
*~
# Исключить все файлы с расширением .a
*.a
# Но отслеживать файл lib.a даже если он подпадает под исключение выше
!lib.a
# Исключить файл TODO в корневом каталоге, но не файл в subdir/TODO
/TODO
# Игнорировать все файлы в каталоге build/
build/
# Игнорировать файл doc/notes.txt, но не файл doc/server/arch.txt
doc/*.txt
# Игнорировать все .txt файлы в каталоге doc/
doc/**/*.txt
```

> [!info]
> В простейшем случае репозиторий будет иметь один файл .gitignore в корневом каталоге, правило из которого будут рекурсивно применяться ко всем подкаталогам. Так же возможно использовать *.gitignore* файлы в подкаталогах. Правило из этих файлов будут применяться только к каталогам, которых они находятся.

source: [github-doc](https://github.com/github/gitignore)


# Удаление файлов
---
```bash
git rm
```
- Удаляет файл из рабочего каталога и из отслеживаемых в git
    - В качестве параметров можно передавать:
        - файлы
        - каталоги
        - шаблоны
