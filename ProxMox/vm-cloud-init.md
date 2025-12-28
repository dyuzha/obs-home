---
id: vm-cloud-init
aliases:
  - Настройка Cloud Init
tags: []
---

# Настройка Cloud Init
---

## Просмотр настроек
---
```bash
qm cloudinit dump 3000 user
qm cloudinit dump 3000 network
qm cloudinit dump 3000 meta
```

## Инициализация
---

```bash
# Имортируем qcow для cloud-init
qm importdisk 100 /var/lib/vz/template/qcow2/CentOS-Stream-GenericCloud-10.qcow2 local-lvm

# Настраиваем загрузку с него
qm set 100 --boot c --bootdisk scsi0

# Подключаем модуль cloud-init
qm set 100 --ide1 local-lvm:cloud-init
```
Дополнительно

```bash
# Настраиваем сеть
qm set 3000 --ipconfig0 "ip=dhcp"

# Включаем агент
qm set 3000 --agent enabled=1
```

## Настройка
---

### Настройка пользователя
---
```bash
# Инициализировать ssh пользователя
qm set 100 --ciuser username --cipassword "secret"

# Прокинуть ssh ключи
qm set 100  --sshkeys ~/.ssh/id_rsa.pub
```
