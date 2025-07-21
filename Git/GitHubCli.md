---
id: GitHubCli
aliases:
  - GitHub CLI
tags: []
---
# GitHub CLI
---

## Init
---
```bash
# Install
dnf install gh

# Authent..
gh auth login
```
После этого начнется интерактивная авторизация...

## Первые шаги
---
```bash
# Вывести список repo
gh repo list

# Редактирование настроек
gh repo edit <owner/repo>

# Удаление
gh repo delete <owner/repo>
```

## Кейсы
---
```bash
# Добавить на gh новый репозиторий (в котором сейчас находишься)
gh repo create <name-repo> --public --push --source .
```

---
Отправить созданный repo на гитхаб
```bash
gh repo create radical --description "CalDAV/CardDAV-srv" --public --source=. --remote=origin --push
```




