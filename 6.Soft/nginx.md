---
id: nginx
aliases:
  - Все, что лежит в conf.d/ с раширением .conf, автоматически подключается
tags: []
---

`/etc/nginx`:

## / nginx.conf
---
Главный конфигурационный файл.

- подключает остальные конфиги (`includes`)
- задает глобальные параметры
- содержит блоки:
    - `events`
    - `http`
    - иногда `stream`

### Логическая структура
---
```bash
user www-data;
worker_processes auto;

# Отвечает за:
#     - соединения;
#     - количество воркеров;
#     - производительность;
events {
    worker_connections 1024;
}

# Все что связано с:
#     - web-серера;
#     - виртуальные хосты (server);
#     - location;
#     - proxy;
#     - gzip;
#     - логи;
http {
    include mime.types;
    default_type application/octet-stream;

    include /etc/nginc/conf.d/*.conf;
    include /etc/nginc/sites-enabled/*;

}
```


## / conf.d/
---
Папка для дополнительных конфигов.
Обычно подключают в `nginx.conf`

```nginx.conf
include /etc/nginx/conf.d/*.conf;
# Все, что лежит в conf.d/ с раширением .conf, автоматически подключается
```

## / sites-available/
---
Все конфигурации сайтов.
```bash
example.com
api.example.com
test.local
```

## / sites-enabled/
---
Символические ссылки на активные сайты.

Активация сайта:
```bash
ln -s /etc/nginx/sites-available/example.com \
    /etc/nginx/sites-enabled
```
Позволяет включать/выключать сайты без удаления конфигов.

## / snippets/
---
Необольшие повторно используемые куски конфигурации
```bash
ssl-params.conf
fastcgi-php.conf
security-headers.conf
```

# Команды
---
```bash
# Проверка конфига
nginx -t

# Перезагрузка (мягкая)
systemctl reload nginx

# Полный рестарт
systemctl restart nginx
```
