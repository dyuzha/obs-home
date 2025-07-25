---
id: Conflicts
aliases:
  - Решение конфликтов
tags: []
---
**Back**
	[[Git]]

# Решение конфликтов
---

## Причины конфликтов:
---
- Вносимые конкурирующие изменения в ту же строку файла
- Один и тот же файл:
    - изменили (один пользователь)
    - и удалили (другой пользователь)

## Способ разрешить конфликты.
---
1. Открыть терминал
2. Перейти в локальный *Git* репозиторий.
3. `git status` - так можно будет увидеть в каком файле(ах) произошел конфлинкт слияния.
4. Открыть файл с конфлиутом в редакторе.
5. Расшифровка:

> [!Summary] Conflicts file

```bash
Общее..
<<<<<< HEAD
версия одной ветки
======
версия другой ветки
>>>>>> branch-name
```
6. Необходимо привести данный файл в желаемый вид
	=> После чего проиндексировать и закомитить

Источник: [GitHub - Разрешение конфликтов слияния](https://docs.github.com/ru/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line)

## Анализ
---
```bash
git diff branch1 branch2 # Показать все разоичия
git diff --name-only branch1 branch2 # Показать имена файлов с различиями
```

## Посмотреть конфликты при слиянии
---
```bash
git merge --no-commit --no-ff origin/main
git status
# После просмотра отменить слияние
git merge --abort
```


