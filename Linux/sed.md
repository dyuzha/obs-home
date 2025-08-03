---
id: sed
aliases:
  - sed
tags: []
---
**Back**
    [[!Lin]]

# sed
---
Stream EDitor
Текстовоый потоковый редактор в Linux, предназначенный для обработки и преобразования текста построчно.
- Поиск и замена текста
- Удаление строк
- Вставка текста
- Выборка определенный строк
- применение сложных скриптовых преобразований

```bash
sed [opt] 'command' <file>

some-command | sed 'command'
```
**Опция -i меняет исходный файл, без нее файл не поменятся**


## Замена текста
---
```bash
sed 's/old/new/' file.txt       # Замена первого вхождения в строке
sed 's/old/new/g' file.txt      # Замена всех вхождений (глобально)
sed 's/old/new/2' file.txt      # Замена только 2-го вхождкния в строке
sed 's/old/new/i' file.txt      # Без учета регистра

echo 'Hello World' | sed 's/World/Linux'
# Hello Linux
```

## Удаление строк
---
```bash
sed '3d' file.txt               # Удалить 3-ю строку
sed '1,5d' file.txt             # Удалить строки с 1 по 5
sed '/pattern/d' file.txt       # Удалить строки, содержащие "pattern"
sed '/^$/d' file.txt            # Удалить пустые строки (^ - начало строки, $-конец)
```
