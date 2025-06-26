---
id: cases
aliases:
  - Cases
tags: []
---

# Cases
---

## Удалить файл из отслеживаемых
---
```bash
git rm --cached <file>
```


## Изменить права на фалы
---
```bash
chmod +x scripts/*.sh
git add --chmod=+x scripts/*.sh
git commit -m "Add executable scripts"

# Проверка текущиъ прав в git
git ls-files --stage scripts/*.sh
```


##
---
