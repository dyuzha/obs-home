---
id: update
aliases:
  - Обновление 8.X.X. -> 9.X.X.
tags: []
---

# Обновление 8.X.X. -> 9.X.X.
---


## Основные команды
---

```bash
# Показывает ошибки и предупреждения для успешного обновления
pve8to9 --full

# Посмотреть версию
pveversion

# Выполнить обновление
apt dist-upgrade
```

## Вспомогательные команды
---

```bash
# Обязательно необходимо заменить старые репозитории на новые
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/*.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/*.sources

# Проверка
grep -r "bookworm" /etc/apt/sources.list /etc/apt/sources.list.d/

# Обновить пакеты
apt update && upgrade

# Ругался на это
apt remove systemd-boot
apt install intel-microcode
```
