---
id: Write_file
aliases:
  - Запись в файлы
tags: []
---


# Запись в файлы
---

## Дозаписать в файл с правими root
---
```bash
echo "some text" | sudo tee -a /file/with/sudo/permited
# or
sudo sh -c `echo "some text" >> /file/with/sudo/permited`
```
