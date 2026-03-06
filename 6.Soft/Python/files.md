---
id: files
aliases: []
tags: []
---
**Back**
    [[!Python]]

# Работа с файлами
---
>[!Example]
```python
f = open('file-nm', '<mode>', encoding='кодировка') # opt: mode = rt
f.close()

# или так
with open('file.txt', 'r+', encoding='utf-8') as f:
    pass
    # Файл автоматически закроется
```

| Mode | Description                                          |
|------|------------------------------------------------------|
| r    | Reed (opt)                                           |
| r+   | Read and Wright                                      |
| w    | Wright                                               |
| w+   | Wright (Перезаписывает файл)                          |
| x    | Wright, if the file do is not exist called exception |
| a    | Anal '>>' in unix (Дозаписывает)                      |
| b    | Open in blob mode                                    |
| t    | Open in text mode (opt)                              |
