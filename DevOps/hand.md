---
id: hand
aliases: []
tags: []
---

```bash
docker run -d -p 8080:80 docker/welcome-to-docker

-d
-p


```

# Container
```bash
docker container
    ls      # Отображает все доступные контейнеры
    start   # Активирует существующие команды
    run     # Создает контейнер и сразу включает его
    inspect # Подробнее рассказывает о существующем контейнере
#
```

# Образы
---
```bash
# Посмотреть все образы
docker images

# Собрать образ
docker build -t {local_name}
# or
docker build -t {name_part1/name_part2} # (public_name)
```
