---
id: cases
aliases:
  - Docker Cases
tags: []
---


# Docker Cases
---

## Не поднимается контейнер
---

```bash
# Запустите в режиме verbose, чтобы увидеть все ошибки
docker compose --verbose up nextcloud 2>&1 | head -100
# Перенаправляет только поток ошибок в консоль (Первые 100 строк)
```

Занятые порты
```bash
# Проверьте, не занят ли порт 80 или 443
netstat -tulpn | grep -E ":80 |:443 "
```

Вывести всю детальную информацию, фильтр
```bash
docker inspect nextcloud-mariadb | grep -A 10 Health
```


```bash
# адрес шлюза
ip addr show docker0
172.17.0.1/16
# Его можно указывать, чтобы достучаться до приложения на хосте
```
