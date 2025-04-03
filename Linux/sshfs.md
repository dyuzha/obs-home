---
id: sshfs
aliases: []
tags: []
---
**Back**
    [[!Lin]]

# sshfs
---
Утилита для монтирования удаленной файловой системы
Можно использовать для редактирования конфигов любимым редактором

```bash
# Монтирование
sshfs remote-user@remote-server.com:/home/remote-user/ ~/mnt

# Размонтирование
fusermount -u ~/mnt
```

