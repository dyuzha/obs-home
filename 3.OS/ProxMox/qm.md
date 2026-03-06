---
id: "!PM"
aliases:
  - QM
tags: []
---

**More**
    [[virtio]]


# QM
---
QEMU/KVM Manager, основной CLI инструмент для управления виртуальными машинами

## Основные команды
---

### Базовое управление
---
[[vm-base-manage]]

```bash
qm create 100       # Изменить настройки
qm clone 100 200    # Показать конфиг
qm descroy 100      # Удалить VM

qm start 100        # Запустить VM
qm stop 100         # Остановить VM
qm reset 100        # Перезагрузить VM
qm shutdown 100     # Корректно выключить
```

### Конфигурация
---
[[vm-set-disk]]
[[vm-set-graphic]]
[[vm-set-rng]]
[[vm-set-net]]
[[vm-cloud-init]]

```bash
qm set 100 ...      # Изменить настройки
qm config 100       # Показать конфиг
qm resize 100 ...   # Изменить размер диска
```

Обязательно подключаем RNG (за очень редким исключением)!
```bash
# Можно ограничить скорость (чтобы не нагружать хост)
qm set 100 --rng0 max-bytes=1024,period=1000
# max-bytes: байт в период
# period: миллисекунды между запросами
```

### Диски
---
```bash
qm importdisk 100   # Импорт диска
qm disk import 100  # Импорт диска (Альтернатива)
qm move-disk 100    # Переместить диск
```


## Передача аргументов QEMU напрямую
---
`--args` позволяет передать аргументы QEMU, напрямую, минуя proxmox обертку

Когда используется:
- Эксперементальные фичи (Proxmox еще не поддерживает)
- Специфичные параметры QEMU
- Отладка проблем с GPU Passthrough
- Обход багов в обертке Proxmox


Риски:
```bash
# Легко сломать
qm set 100 --args "-device wrong-param"  # VM не запустится

# Конфликт с настройками Proxmox
qm set 100 --hostpci0 01:00.0 --args "-device vfio-pci,host=01:00.0"
# Дублирование! Будет две видеокарты
```

## Примеры
---

### Создание VM Centos 10 stream для Cloud-Init
---
1. Создание vm
```bash
qm create 3000 \
    --name "Centos-10-stream.cloud" \
    --memory 2048 \
    --cores 2 \
    --net0 virtio,bridge=vmbr0
```

2. Импорт cloud-init образа
```bash
qm importdisk 3000 /var/lib/vz/template/qcow2/CentOS-Stream-GenericCloud-10.qcow2 local-lvm
```

3. Настройка
```bash
# Прикрепляем диски
qm set 3000 --scsihw virtio-scsi-pci --scsi0 local-lvm:vm-3000-disk-0
qm set 3000 --ide2 local-lvm:cloudinit

# Настраиваем загрузку с импортированного диска
qm set 3000 --boot c --bootdisk scsi0

# Настраиваем графику через виртуальный последовательный (com) порт
qm set 3000 --serial0 socket --vga serial0

# Настраиваем сеть через dhcp
qm set 3000 --ipconfig0 "ip=dhcp" --nameserver "77.88.8.8"

# Включаем QEMU Agent
qm set 3000 --agent enabled=1
```

4. Запуск
```bash
qm start 3000
```

5. Проверка
```bash
qm status 3000
```
