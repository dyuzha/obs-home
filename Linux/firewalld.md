---
id: firewalld
aliases:
  - firewalld
tags: []
---

# firewalld
---
Открыть порт для k8s
```bash
# 1. Сначала узнайте ваш текущий публичный IP
# На вашей локальной машине (PROF-07) выполните:
curl ifconfig.me
# Или
curl icanhazip.com

# Предположим, ваш IP: 88.147.152.206

# 2. На сервере srv-3 создайте зону для вашего IP
sudo firewall-cmd --permanent --new-zone=k8s-access

# 3. Добавьте ваш IP в зону
sudo firewall-cmd --permanent --zone=k8s-access --add-source=ВАШ_IP/32
# Например:
sudo firewall-cmd --permanent --zone=k8s-access --add-source=88.147.152.206/32

# 4. Откройте порт 6443 только в этой зоне
sudo firewall-cmd --permanent --zone=k8s-access --add-port=6443/tcp

# 5. Убедитесь, что в публичной зоне порт 6443 ЗАКРЫТ
sudo firewall-cmd --permanent --remove-port=6443/tcp --zone=public 2>/dev/null || true

# 6. Примените изменения
sudo firewall-cmd --reload

# 7. Проверьте настройки
sudo firewall-cmd --zone=k8s-access --list-all
```
