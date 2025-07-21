---
id: gh-actions
aliases:
  - gh-actions
tags: []
---
**Back**
    [[!!Base]]
    [[ci_cd]]
    [[workflow]]

# gh-actions
---

```yaml
name: Test Bash Scripts

on: [push, pull_request]

jobs:
    test:
        runs-on: ubuntu-latest
        steps:
            - users: actions/chechout@v4
            - name: Build Docker image
                run: docker build -t bash-tester -f Dockerfile .
            - name: Run tests
                run: docker run --rm bash-tester bats tests/
```

Встроенная в GitHub система CI/CD (Непрерывной интеграции и доставки), которая позволяет автоматизировать
- сборку
- тестирование
- развертывание кода
прямо из репизитория

Автоматизация рутинных задач (тесты, линтинг, сборка)
Запуск задач на событиях (push, pull_request, cron)
Интеграция с Docker, Kubernetes, облачными провайдерами (AWS, Azure, GCP)
 Бесплатно для публичных репозиториев (2000 минут в месяц для приватных)

## Основные Компоненты
---

| Компонент | Описание                                                     |
|-----------|--------------------------------------------------------------|
| Workflow  | Автоматизированный процесс (файл .yml в github/workflows/)   |
| Event     | Событие, запускающее workflow (push, pull_request, schedule) |
| Job       | Отдельная задача (test, build, ...)                          |
| Step      | Command ot action (run, uses, ...) IN Job                    |
| Action    | Готовый скрипт (actions/chechout@v4)                         |
| Runner    | Сервер (виртуальная машина), на котором выполняется workflow |


## Workflow
---
1. В репозитории создать папку:
`.github/workflows/`

2. Добавить файл .yml (например, ci.yml)
```yml
name: CI Pipeline
on: [push]  # Триггер

jobs:                                       # Cписок задач
  test:                                     # Задача с именем test
    runs-on: ubuntu-latest                  # OS для запуска
    steps:                                  # Шаги внутри job
      - uses: actions/checkout@v4           # Клонирует репозиторий
      - run: echo "Hello, GitHub Actions!"  # Простая команда

```

## Event
---
### Синтаксис
```yml
on: [push]
on: [push, pull_request]
```

### Вариации
---
```yml
# При пуше в любую ветку
on: [push]

# При создании/обновлении Pull Request
on: [pull_request]

# Анал. `pull_request`, но с правами исходного репозитория
on: [pull_request_target]

# При создании тега или ветки
on: [create]

# При удалении тега или ветки
on: [delete]
```


#### События по расписанию (как cron)
---
```yaml
on:
    schedule:
        - cron: '0 3 * * *' # Каждый день в 3:00 UTC

```


### Примеры
---
```yml
on:
    push:
        branches: [ main ]      # Только при пуше в main
    pull_request:
        branches: [feature/*]   # Только PR в ветке feature/*
```

## Job
---
```yml
jobs:
    test: # Задача с имененем test

```

## Steps
---
```yml
steps:                                  # Шаги внутри job
  - uses: actions/checkout@v4           # Клонирует репозиторий
  - run: echo "Hello, GitHub Actions!"  # Простая команда
```

## Action
---
Готовый скрипт
```yml
uses:                       # Выбрать действие из маркетплейса

uses: actions/checkout      # Название действия
                            # (репозиторий actions/checkout в GitHub).

uses: actions/checkout@v4   # Версия действия.
                            # Всегда используйте актуальную
                            # (на момент написания — v4).
```

### Расширенный вариант
---
```yml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 2          # Клонирует только 2 последних коммита (ускоряет работу)
      submodules: recursive   # Подтягивает submodules
      ref: 'my-branch'       # Клонирует конкретную ветку (по умолчанию — текущую)
```

### Приватный репо
---
```yml
steps:
  - uses: actions/checkout@v4
    with:
      repository: 'org/private-repo'
      token: ${{ secrets.GH_PAT }}  # Personal Access Token с правами repo
```


1. Добавление секретов
```bash
# Если не авторизован
gh auth login

# Перейти в корень репозитория
cd /path/to/repo

# Добавление секретов
gh secret set CF_Token --body "cf_api_token"
gh secret set CF_Account_ID --body "cf_account_id"

# Прверка
gh secret list

# Проверка работоспособности
gh workflow run "ACME SSL Certificate Management"

# Проверка логов
gh run watch

```
