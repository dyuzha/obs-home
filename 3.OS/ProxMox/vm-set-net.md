---
id: vm-set-net
aliases:
  - Настройки сети
tags: []
---


# Настройки сети
---

```bash
# Задать dhcp
qm set 3000 --ipconfig0 "ip=dhcp"

# Задать IP адрес, шлюз
qm set 3000 --ipconfig0 "ip=192.168.88.100/24,gw=192.168.88.1"
```
