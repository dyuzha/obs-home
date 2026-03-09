---
id: ufw
aliases:
  - UFW
tags: []
---

# UFW
---
Uncomplicated Firewall - простой фронтенд для управления iptables/nftables
Максимально простая модель мез сложных абстракций

Архитектура:

**CLI** - `ufw` ->
-> конфигурация UFW ->
-> iptables / nftables rules ->
-> kernel netfilter

Простой список правил сверху вниз
3 базовые политики:
1. default policy
2. allow
3. deny


## Default policy
---
Политика по умолчанию

```bash
# Активировать
ufw enable

# Посмотреть отчет
ufw status verbose

# Добавить порт
ufw allow in 443
```
