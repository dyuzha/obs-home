---
id: drivers
aliases:
  - drivers
tags: []
---

# drivers
---
Драйвер в Docker - это модули, которые управляют различными аспектами работы контейнеров.
- Хранения данных (тома, файловая система)
- Сеть (тип подключения контейеров)
- Логирование (куда и как пишутся логи)
- Вычислитеотные ресурсы (GPU, CPU)


## Логирования
---
Определяет куда и в каком формате сохраняются логи контейнеров
| Driver    | Description                        | Expend                          |
|-----------|------------------------------------|---------------------------------|
| json-file | Логи в JSON-файлах на хостк (def)  | Разработка, демо-среды          |
| journald  | Логи в systemd (journalctl)        | Linyx-серверы с systemd         |
| syslog    | Отправка логов на удаленный сервер | Центризованный сбор логов       |
| gelf      | Формат для Graylog/ELK             | Стек мониторинга (ELK, Grafana) |
| awslogs   | Логи в AWS CloudWatch              | Развертывание в Amazon          |
| none      | Логи отключены                     | Контейнеры, где логи не нужны   |

Пример настройки
```docker-compose.yml
services:
    app:
        image: nginx
        logging:
            driver: syslog
            options:
            syslog-address: "udp://logs.example.com:514"
```


## Томов (Volume drivers)
---
Управляет хранением данных контейнеров

| Drivers | Description                    |
|---------|--------------------------------|
| local   | Локальные файлы на хостк (def) |
| nfs     | Монтирование NFS-шары          |
| aws     | Тома в EBS                     |
| ceph    | Хранение в CephFS              |

```bash
docker volume create \
        --driver local \
        --opt type=nfs \
        --opt device=:/nfs-share \
        nfs-volume
```


## Драйверы сети (Network Drivers)
---

| Drivers | Description                                                 |
|---------|-------------------------------------------------------------|
| bridge  | Виртуальная сеть между контейнерами (def)                   |
| host    | Контейнер использует сеть хоста (высокая производительност) |
| overlay | Сеть для кластеров (Docker Swarm, Kubernetes)               |
| macvlan | Контейнер получает реальный MAC-адрес                       |
| none    | Сеть отключена (только loopback)                            |

Пример:
```docker-compose.yml
services:
    web:
        image: nginx
        networks:
            - my-network

networks:
    my-network:
    driver: macvlan
    driver_opts:
        parent: eth0
```

## Драйверы хранилищ (Storage Drivers)
---
Управляют файловой системой контейров. Влияют на производительность

| Drivers  | Description             |
|----------|-------------------------|
| overlay2 | Современные Linux (def) |
| aufs     | Устаревший              |
| btrfs    | Для BTRFS               |
| zfs      | Для ZFS                 |

Как проверить текущий драйвер
```bash
docker info | grep "Storage Driver"
```

## Драйверы для GPU (NVIDIA, CUDA)
---
Позволяют контейнерам использовать видеокарты для вычислений
Пример для NVIDIA
```yml
services:
    tensorflow:
        image: tensorflow/tensorflow:latest-gpu
        deploy:
            resources:
                reservations:
                    devices:
                        - driver: nvidia
                        count: 1
                        capabilities: [gpu]
```
