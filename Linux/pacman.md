---
id: pacman
aliases: []
tags: []
---
**Back**
    [[!Lin]]
  [[Packet-mn]]

# Pacman
---

# Cases
---
>[!Example]
```bash
# Показывает AUR пакеты
pacman -Qm

# Удаление кеша
pacman -Scc

# Показывает пакеты сироты
pacman -Qtdq

# Удаление пакетов сирот
pacman -Qt(t)dq | pacman -Rns

# Remove dependencies
pacman -Rs
```
