**Back** 
  [[Packet-mn]]

## Base
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
