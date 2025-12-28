---
id: "!PM"
aliases:
  - PVE
tags: []
---

# PVE
---
Proxmox Virtual Environment (Proxmox VE)

Платформа виртуализации с открытым исходным кодом.

## Структура
---

### 1.  Ядро и ОС
---
- Debian
- Модифицированное ядро

### 2. Гипервизоры
---
- KVM (Kernel-based Virtual Machine) - для VM
- LXC (Linux Containers) - для контейнеров

### 3. Хранилище
---
pve-storage - абстракция над разными типами:
- LVM-Thin
- ZFS
- Ceph
- NFS
- iSCSI
- CIFS/SMB

### 4. Сеть
---
Linux bridges + Open vSwitch
SDN (Software Defined Networking)
// pve-firewall (брандмауэр)

### 5. Управление
---
pveproxy - Веб интерфейс (ReactJS)
pvedaemon - Фоновый демон
pve-cluster - Кластерный менеджер
corosync + pacemaker - Кластеризация

### 6. Инструменты CLI
---
[[qm]] - Управление VM (QEMU/KVM)
pct - Управление LXC контейнерами
pvesh - API клиент
pveceph - Управление Ceph
vzdump - Бекапы
ha-manager - управление HA группами
