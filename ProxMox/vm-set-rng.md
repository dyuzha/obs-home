---
id: vm-settings-rng
aliases:
  - vm-settings-rng
  - RNG
  - Настройки RNG
tags: []
---

# Настройки RNG
---
Генератор случайных чисел

Используется для повышения **Энтропии**.
**Энтропия** - мера случайности, которую питает генератор случайных чисел.

Пробоема vm: **мало источников энтропии**
- Нет реального железа - нет HID событий
- Диски виртуальные - предсказуемые тайминги
- Сеть виртуальная - предсказуемые пакеты

 Решения:
 - ViryIO RNG (в Proxmox)

```bash
# Берет энтропию с хоста
qm set 100 --rng0 /dev/urandom
```
2. haveged (в гостевой ОС)
```bash
# Генерирует энтропию из таймингов CPU
apt install haveged
systemstl enable haveged
```
3. rng-tools
```bash
apt install rng-tools
# Использует /dev/hwrng если есть
```

Проверить энтропию:
```bash
# Сколько доступно прямо сейчас
cat /proc/sys/kernel/random/entropy_avail
# Хорошо: >1000, Плохо: <100

# Пул энтропии
cat /proc/sys/kernel/random/poolsize
# 4096 bits (типично)
```

Источники:
```bash
# Можно ограничить скорость (чтобы не нагружать хост)
qm set 100 --rng0 max-bytes=1024,period=1000
# max-bytes: байт в период
# period: миллисекунды между запросами
```


