---
id: sparse-checkout
aliases:
  - sparse-checkout
tags: []
---
**Back**
    [[!Git]]

# sparse-checkout
---
Локальная операция. Сервер отдает весь репозиторий, но клиент его фильтрует

## Cases
---

### 1. Работа только с одной папкой
---
```bash
# Клонируем репозиторий без файлов
git clone --filter=blob:none --no-checkout https://github.com/dyuzha/.dotfiles
cd .dotfiles

# Включаем sparse-checkout, указываем нужную ветку
git sparse-checkout init --cone
git sparse-checkout set nvim

# Делаем checkout
git checkout master
```

### 2. Добавление папок в существующий sparse-checkout клон репозитория
---
Дополнениени к (1)

```bash
# Перейти в нужную папку
cd .dotfiles

# Добавление новой папки в sparse-checkout
git sparse-checkout add ranger

# Обновить рабочую директорию
git pull origin master

# Проверка
git sparse-checkout list
#... Должны быть нужные папки
```


