---
id: poetry
aliases: []
tags: []
---
**Back**
    [[!Python]]

# Poetry
---
Инструмент для управления проектами Python
- управление зависимостями с воспроизводными установками и резолвом конфликтов
- автоматическое управление виртуальными окружениями
- сборка и публикация


## Инициализация проекта
---
```bash
# Создание нового проекта
poetry new <project-name>
# Создасться директория с такой структурой
project-name/
├── README.md
├── my_project
│   └── __init__.py
├── pyproject.toml
└── tests
    └── __init__.py

# Инициалилизация poetry в ужесуществующем проекте
cd project-name
poetry init
```
Данные команды не создают виртуального окружения


## Виртуальное окружение
---
При первом выполнении команд, связанных с установкой зависимостей, Poetry создает виртуальное окружение, выбрав базовый интерпретатор по следующей логики:
1. Poetry проверяет, активировано ли уже какое-то виртуальное окружение.
Если да, то оно будет использовано
2. Если никакое окружение не активированно, то Poetry попытается использовать Python, который был использован при установке Poetry
3. Если версия Python не совместима с версией, указанной в pyproject.toml, то Poetry попросит явно активировать нужную версию.

Рекомендуется явно указывать базовый интерпритатор для poetry
```bash
# Создает виртуальное окружение с конкретным интерпритатором
poetry env use python3.11 # Если python3.11 есть в PATH
poetry env use /path/to/python # Можно указать полный путь
```

## Файлы
---

### pyproject.toml
---
Файл содержащий в себе всю информацию о проекте:
- Метаданные (имя, версия, лицензия...)
- Зависимости
- Настройки сторонних интсрументов


### poetry.lock
---
Содержит в себе ВСЕ зависимости с ЗАФИКСИРОВННЫМИ версиями
- формируется автоматически (НЕ РЕДАКТИРОВАИТЬ)


### tool.poetry
---
Содержит метаданные
- name
- version
- description
- license
- authors

### tool.poetry.dependencies
---
Содержит в себе версию Python и основные зависисмости (main-группу)

## Команды
---
```bash
# Установка зависимости
poetry add <name-dependencies>

```
