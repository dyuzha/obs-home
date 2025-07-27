---
id: Git
aliases:
  - Git
tags: []
---

# Git
---
## Теория про **Git**
---
[[Base]]
- Базовая информация про **Git**
- Создание **Git** репозитория
- Базовая информация про команду **Git config**
- Первые действия после установки **Git**
- Как пользоваться справкой **help**

[[Merge]]

[[Reference]]
- Инициализация репозитория
- `git status`
- `git diff`
- `git remove`
- `git log`
- `git remote`
- Файл **.gitignore**
- Удаление файлов

[[sparse-checkout]]

[[Stage]]

[[Stash]]

```bash
# Объединить коммиты с предыдущим (чтобы история была чище и короче)
git rebase -i HEAD~n
# n-номер коммита с конца
```

```bash
git reset --soft HEAD~n # Перемещает коммиты -> в index
git reset --hard HEAD~n # Удаляет коммиты
git reset --mixed HEAD~n # Перемещает коммиты -> в unstaged
# n-номер коммита с конца
```


```bash
git config pull.rebase false  # Устанавливает стратегию "merge" по умолчанию
git config pull.rebase true  # Устанавливает стратегию "rebase" по умолчанию
git config pull.ff only  # Разрешает pull ТОЛЬКО если возможен fast-forward

# ---

git pull --no-rebase    # Принудительно merge (даже если rebase=true в настройках)
git pull --rebase       # Принудительно rebase (даже если rebase=false)
git pull --ff-only      # Только fast-forward (отменит pull, если ветки разошлись)
```


## Полезные кейсы
---
[[Cases]]
- Удалить файл из отслеживаемых
- [[ssh]]
    - Как осуществить подключение по ssh
- [[Conflicts]]
    - Разрешения конфликтов


## Приложения для взаимодействия с **Git**
---
[[Lazy Git]]
- TUI для git

[[GitHubCli]]
- TUI для GitHub
