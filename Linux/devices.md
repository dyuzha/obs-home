---
id: cgroups-dev-cons
aliases: []
tags: []
---
**Back**
    [[!Lin]]

# Устройства в Linux
---

```bash
c 1:3 rmw
| |   |
| |   -- Права доступа
| |
| -- Мажорный : Минорный номера устройств
|
--тип устройство (в данном случае символьное)
```

## Типы устойств
---
| Symbol | Description  |
|--------|--------------|
| c      | Символьные   |
| b      | Блочные      |
| a      | Всевозможные |

## Мажорный и минорный номера устройств
---
Узнать номера можно при помощи ls -l /dev/устройство

>[!Example]
```bash
ls -l /dev/null
crw-rw-rw- 1 root root 1, 3 дек 19 15:45 /dev/null
                       |  |
            Мажорный----  ------Минорный
```

## Права доступа
---
| Symbol | Allow                              |
|--------|------------------------------------|
| r      | Читать файлы                       |
| w      | Записывать на указанное устройство |
| m      | создавать новые файлы устройств    |

