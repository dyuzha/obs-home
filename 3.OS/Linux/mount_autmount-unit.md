---
id: mount_autmount-unit
aliases:
  - mount_autmount-unit
  - Mount
  - Mount - unit systemd
tags: []
---
**Back**
    [[!Lin]]
    [[systemd]]
    [[Units]]

# Mount - unit systemd
---
Юнит монтирования
Переносят управление файловыми системами из мира `/etc/fstab` в мир `systemd`.

## Общая идея
---
Соответствует строке в `/etc/fstab`, но управляется через `systemd`.

Название юнита связано с точкой монтирования.
Например:
- `/home` -> `home.mount`;
- `/var/lib/mysql` -> `var-lib-mysql.mount`.

Когда *systemd* видит `.mount`- юнит, он отвечает за монтирование файловой системы.

## Синтаксис
---
```ini
[Unit]
Description=Mount extra data disk

[Mount]

# Что монтируем (Устройство файл или ресурс)
What=server:/share
# What=/dev/sdb1

# Куда монтируем (каталог)
Where=/mnt/data

# Тип ФС (xfs, nfs, ...)
Type=ext4

# Опции монтирования (rw, noatime, ...)
Options=defaults

[Install]
WantedBy=multi-user.target
```


