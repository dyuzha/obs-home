---
id: firewalld
aliases:
  - firewalld
tags: []
---

# firewalld
---
Архитектура:

**CLI** - `firewall-cmd`
**API** - D-Bus
**backend** - iptables (легаси) / nftables
**firewalld** - daemon

firewall-cmd -> D-Bus -> nftables/iptables rules

- Изменение правил без перезагрузки firewall

Основные сущности - **Zones**

## Zones
---
- **trusted** - доверенная сеть
- **home** - домашняя сеть
- **work**  - рабочая
- **public** - публичная
- **drop**  - все дропать

```bash
# Посмотреть зоны
firewall-cmd --get-zones

# Текущая зона интерфейса
firewall-cmd --get-actiove-zones

# Назначить интерфейс зоне
firewall-cmd --zone=public --change-interface=eth0
```
Каждая зона содержит сервисы

## Services
---
**Service** - это предопределенный набор портов и протоколов

```bash
# Посмотреть сервисы
firewall-cmd --get-services

# Добавить сервис
firewall-cmd --zone=public --add-service=http
```

## Порты
---
```bash
# Открыть порт на прямую
firewall-cmd --zone=public --add-port=8080/tcp

# Удалить порт
firewall-cmd --zone=public --remove-port=8080/tcp
```

## Runtime / Permanent
---
firewalld имеет 2 конфигурации

Runtime - действует до перезагрузки
Permanent - сохраняет на диск (просто добавить ключ `--permanent`)
После permanent нужно reload

## Rich Rules
---
Более гибкие правила (аналог `iptables`)

```bash
# Разрешить ssh только с одного IP
firewall-cmd --add-rich-rule=' rule family="ipv4" \
    source address="10.0.0.5 \
    service name="ssh" \
    accept'

# Заблокировать IP
firewall-cmd --add-rich-rule='rule family="ipv4" \
    source address="1.2.3.4" \
    drop'
```

## Masquerade (NAT)
---
 Используется для NAT (???)
```bash
firewall-cmd --zone=public --add-masquerade
```

## Forwarding
---
Перенаправление портов

```bash
firewall-cmd --add-forward-port=port=80:proto=tcp:toport=8080
```




















Открыть порт для конкретного IP на примере k8s
```bash
# 1. Узнайть публичный IP
curl ifconfig.me
# Или
curl icanhazip.com

# 2. Создать зону для вашего IP
sudo firewall-cmd --permanent --new-zone=k8s-access

# 3. Добавить IP в зону
sudo firewall-cmd --permanent --zone=k8s-access --add-source=ВАШ_IP/32
# Например:
sudo firewall-cmd --permanent --zone=k8s-access --add-source=88.147.152.206/32

# 4. Откройте порт 6443 только в этой зоне
sudo firewall-cmd --permanent --zone=k8s-access --add-port=6443/tcp

# 5. Убедитcя, что в публичной зоне порт 6443 ЗАКРЫТ
sudo firewall-cmd --permanent --remove-port=6443/tcp --zone=public 2>/dev/null || true

# 6. Примените изменения
sudo firewall-cmd --reload

# 7. Проверьте настройки
sudo firewall-cmd --zone=k8s-access --list-all
```
