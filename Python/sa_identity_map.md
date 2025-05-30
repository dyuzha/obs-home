---
id: sa_identity_map
aliases:
  - sa_identity_map
  - Identity Map
tags: []
---

# Identity Map
---
Карта идентичности

Паттерн проектирования, используемый в ORM, который гарантирует, что
Каждый объект модели (н-р, `User`) с одним и тем же первичным ключом (`id`) будет представлен в памяти только одним экземпляром `Python` в рамках текущей `session`

- Предотвращает дублирование объектов
- Обеспечивает согласованность данных при работе с ORM
    Если в разных частях кода запрашивается один и тот же User, изменения будут видны везде
- Эффективность
    Не нужно загружать одни и те же данные из БД многократно
- Контроль транзакций
    Все изменнения объекта отслеживаются в рамках одной сессии

## Принцип работы
---
1. При загрузке объекта из бд, например
`session.query(User).get(1)`

- SQLAlchemy сначала проверяет, есть ли объект с `id=1` в кэше сессии (Identity Map)
- Если есть - возвращает тот же самый экземпляр (а не создает новый)
- Если нет - загружает из бд, сохраняет в кэш и возвращает

2. При повторном запросе того же `id` - возвращается кэшированный объект
```python
user1 = session.query(User).get(1)
user2 = session.query(User).get(1)

print(user1 is user2) # True (это один и тот же объект в памяти)
```

## Когда не работает Identity Map
---
1. Удаление объекта из сессии
```python
# Удаляем user1 из Identity Map
session.expunge(user1)
user4 = session.query(User).get(1) # Будет новый объект
print(user1 is user4) # False
```
2. Закрытие сессии
При закрытие сессии, Identity Map очищается

3. При запросе из другой сесии

## Получить свежие данные из бд (гарантированно)
---
```python
# Перезагрузить объект из БД
session.refresh(user1)

# или

# Сбросить весь кеш
session.expire_all()
# Позже повторно загрузить объект
```
