---
id: volumes
aliases:
  - volumes
tags: []
---
**Back**
    [[!Docker]]

# volumes
---
-- Внешнее хранилище данных для контейнера
Тома позволяют отделить данные от контейнеров.


## Виды томов
---

- Анонимные
- Именованные
- Bind mount (Host-монтирование)

### Анонимные тома
---
Создаются автоматически, если в Dockerfile есть VOLUME, но не указано имя
Имеют случайный ID


### Именованные тома
---
Создается вручную, имеют понятное имя
Удобны для управления
```bash
docker volume create mydata # Создаем том
docker run -v mydata:/app/data myapp # Подключаем
```


### Bind mount (Host-монтирование)
---
Связывает папку на хосте с папкой в контейнере
Изменения на хосте видны в контейнере
```bash
docker run -v /home/user/project:/app myapp
```

## Опции
---
| Option      | Description                    |
|-------------|--------------------------------|
| :consistent | Полная синхронизация (default) |
| :delegated  | Контейнер ведет синхронизацию  |
| :cached     | Хост ведет синхронизацию       |


## Команды
---
```bash
# Список всех томов
docker volume ls
# Информация о томе
docker volume inspect mydata
# Удалить том
docker volume rm mydata
# Удаление несипользуемых томов
docker volume prune
```


## Лучшие практики работы с томами
---
Для разработки
```bash
docker run -v $(pwd)/src:/app/src -p3000:3000 node
```

Для production
```bash
docker volume create app_data
docker run -v app_data:/var/www/html nginx
```

Для бд
```bash
docker run -v db_data:/var/lib/postgresql/data \
    -e POSTGRES_PASSWORD=secret \
    postgres
```

Резервное копирование
```bash
docker run --rm -v db_data:/source -v $(pwd):/backup \
    alpine tar cvf /backup/db_backup.tar /source
```
