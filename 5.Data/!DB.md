---
id: "!DB"
aliases:
  - DataBases
tags: []
---

# DataBases
---


## Администрирование
---
1. Установка и настройка
2. Резервное копирование
3. Мониторинг
4. Оптимизация
5. Безопасность

1. postgresql.conf    # Основные настройки
2. pg_hba.conf        # Доступ по сети
3. postmaster.pid     # PID главного процесса
4. pg_wal/            # Журнал транзакций (ваш кошмар!)
5. base/              # Данные таблиц
```bash
# 1. Запуск/остановка
sudo systemctl restart postgresql

# 2. Резервная копия
pg_dump dbname > backup.sql

# 3. Восстановление
psql dbname < backup.sql

# 4. Консоль
sudo -u postgres psql

# 5. Проверка логов
tail -f /var/log/postgresql/postgresql-*.log
```
```sql
-- 1. Кто подключен?
SELECT * FROM pg_stat_activity;

-- 2. Что тормозит?
SELECT query, now() - query_start as duration
FROM pg_stat_activity
WHERE state != 'idle'
ORDER BY duration DESC;

-- 3. Размеры таблиц?
SELECT tablename, pg_size_pretty(pg_total_relation_size(tablename))
FROM pg_tables
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(tablename) DESC;

-- 4. Есть ли блокировки?
SELECT * FROM pg_locks WHERE NOT granted;

-- 5. Статистика БД?
SELECT * FROM pg_stat_database;
```





