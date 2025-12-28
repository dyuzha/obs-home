---
id: disk
aliases:
  - Контроллер диска
  - QM set
  - Контроллер Диска
tags: []
---
**Back**
    [[!PM]]

# Контроллер Диска
---
Эмулирует железо для работы диска в гостевой ОС

## Пример
---
```bash
qm set 100 --scsihw virtio-scsi-pci --scsi0 local-lvm:vm-3000-disk-0
qm set 100 --ide2 local-lvm:cloudinit
```

## Синтаксис
---
Задает тип контроллера для всех **scsi**-дисков 1 раз для всей VM
```bash
qm set 100 --scsihw ...
```
Прикрепляет определенный диск
```bash
qm set 100 --... хранилище:диск с номером
```

## Теория
---

### Тип контроллера
---
Для данных дисков выбирать не нужно:
    IDE - тип контроллера **фиксированный**
    VirtIO - тип контроллера **фиксированный**
    SATA - тип контроллера **фиксированный**

Для дисков SCSI:

Linux:
| Name               | Value             | Luns (факт.) | Description       |
|--------------------|-------------------|--------------|-------------------|
| VirtIO SCSI        | `virtio-scsi-pci` | 256 (32)     | Современный Linux |
| VirtIO SCSI single | `virtio-scsi-pci` | 1            | Старые гости      |

WMWare:
| Name                    | Value     | Luns (факт.) | Description                        |
|-------------------------|-----------|--------------|------------------------------------|
| LSI MegaRAID SAS        | `megasas` | 256 (16)     | VMware Workstation, Windows WMware |
| VMWare Paravirtual SCSI | `pvscsi`  | 64 (16)      | VMware ESXI гости, Linux WMware    |

Легаси
| Name          | Value       | Luns (факт.) | Description                    |
|---------------|-------------|--------------|--------------------------------|
| LSI Logic SAS | `lsi`       | 8            | Стандартная совместимость      |
| LSI 53C810    | `lsi53c810` | 8            | Совместимость эпохи диназавров |


## Диски

- Цифра — это порядковый номер диска на конкретном виртуальном контроллере.
- Cloud-init - всегда на IDE2
- Можно прикрутить несколько разных контроллеров для одной **vm**

| Name         | Command     | driver      | Count | Description       |
|--------------|-------------|-------------|-------|-------------------|
| SCSI         | `--scsi0`   | virtio-scsi | 0-31  | Современный Linux |
| VirtIO Block | `--virtio0` | virtio-blk  | 0-31  | Устаревший Linux  |
| IDE          | `--ide0`    | Встроенный  | 0-3   | Windows / Legacy  |
| SATA         | `--sata0`   | ahci        | 0-5   | Универсальный      |


### Варианты использования нескольких контроллеров
---

Linux + Windows в dual-boot (Для энтузиастов)
```bash
qm set 100 --scsi0 local-lvm:linux-disk
qm set 100 --ide0 local-lvm:windows-disk
```

Загрузка, установка
```bash
qm set 100 --ide0 local:iso/ubuntu.iso      # ISO для установки
qm set 100 --scsi0 local:iso/system-disk    # ISO для установки
```

Legacy оборудование в VM
```bash
qm set 100 --ide0 local-lvm:legacy-app-disk
qm set 100 --scsi0 local-lvm:fast-data-disk
```

Cloud-init (требует IDE2)
```bash
qm set 100 --ide2 local-lvm:cloudinit
qm set 100 --scsi0 local-lvm:system-disk
```

Разные типы хранилищ
```bash
# SSD для системы (SCSI)
qm set 100 --scsi0 ssd-pool:fast-disk
# HDD для данных (VirtIO)
qm set 100 --virtio0 hdd-pool:data-disk
# CD-ROM для образов (IDE)
qm set 100 --ide0 local:iso
```

Медиа-сервер
```bash
# Система на быстром SSD (SCSI)
qm set 101 --scsi0 ssd-pool:system-disk

# Фильмы на большом HDD (SATA)
qm set 101 --sata0 hdd-pool:movies-disk

# Музыка на втором HDD (VirtIO)
qm set 101 --virtio0 hdd-pool:music-disk

# Cloud-init для управления (IDE2)
qm set 101 --ide2 local-lvm:cloudinit
```

