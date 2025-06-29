---
id: Bash
aliases:
  - Примеры использования
tags: []
---

# Примеры использования
---

```bash
# Устанавливаем права доступа к скопированным файлам и папкам
find "$HOME" -type f -exec chmod 644 {} \;
find "$HOME" -type d -exec chmod 755 {} \;

# Добавляем папку bin в переменную PATH
export PATH="$PATH:$HOME/.dotfiles/bin"
```


# Syntax
---

## Операторы сравнения
---

| Command | Action           |
|---------|------------------|
| -eq     | равно            |
| -ne     | не равно         |
| -gt     | больше           |
| -lt     | меньше           |
| -ge     | больше или равно |
| -le     | меньше или равно |
| -a      | And              |
| -o      | Or               |


>[!Example]
```
[ "$a" -le "$b" ]
```


| Command | Action           |
|---------|------------------|
| <       | меньше           |
| <=      | меньше           |
| >       | больше           |
| >=      | больше или равно |
| &&      | And              |

| `||`    | или              |

>[!Example]
```
(("$a" < "$b"))
```


## Конструкция CASE
---
```bash
fruit="apple"

case $fruit in
  "apple") echo "Это яблоко";;
  "banana") echo "Это банан";;
  *) echo "Неизвестный фрукт";;
esac
```
