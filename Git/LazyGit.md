---
id: LazyGit
aliases:
  - Ranger
tags: []
---
**Back**
	[[Git]]

# Ranger
---

## Rebase
---
Объединить коммиты с предыдущим (чтобы история была чище и короче)

Аналогично
```bash
git rebase -i HEAD~n
# n-номер коммита с конца
```


## Reset
---
Переместить коммит в индекс
```bash
git reset --soft HEAD~n
# n-номер коммита с конца
```




