---
id: sa_select
aliases: []
tags: []
---
**Back**
    [[sqlalchemy]]


# Запросы к бд
---

## Основные способы выполнения запросов
---
### Query
Старый стиль
```python
from sqlalchemy.orm import Query
query = Query(User).filter_by(name='Alice')
users = db.session.execute(query).scalars().all()
```
| Method                 | Return                       |
|-----------------------|------------------------------|
| .scalars()      | Список ORM объектов           |
| .scalar()             | Одно значение (первый столбец)|
| .execute().fetchall() | Список строк                 |
| .execute().mappings() | Список словарей              |

### .scalars()
---
Возвращает список ORM - объектов
- Конвертирует каждую строку результата в объект модели
- Подходит для запросов select(Model)

```python
# Вернет все записи в виде ORM объектов
users = session.scalars(select(User)).all()

# Вернет один объект или None
users = session.scalars(select(User)).first()

# Вместо all, для потокового вывода
for user in session.scalars(select(User).yield_per(100)):
    process(user)
```

### .scalar()
---
Возвращает одно значение (первый столбец первой строки) или None
- Используется для агрегатных функций (`count()`, `sun()`)
- Когда нужен один конкретный столбец
```python
count = session.scalar(select(func.count(User.id)))
```

### .execute()
---
Возвращает сырые данные из бд
- Исопльзуется, когда не нужные ORM-объекты
н-р, для сырых SQL-запросов

```python
result = session.execute(select(User.id, User.name))

# Возвращает список кортежей
rows = result.fetchall() # [(1, 'Alice'), (2, 'Bob')]

# Возвращает список словарей
rows = result.mappings().all()
# [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]

```

## Методы выполнения запросов

 | Метод             | Уровень  | Возвращаемый тип |
 |-------------------|----------|------------------|
 | .all()            | ORM      | Список           |
 | .yield_per(N)     | ORM      | Итератор         |

### .yield_per(N)
---
Инструмент для эффективной потоковой обработки больших объемов данных из бд
Оптимизирует потребление памяти при работе с большими результатами запросов.
- Разбивает результат на "пакеты" (батчи) указанного размера
- Не загружает все строки в память
- Подходит для обработки миллионов записей без риска переполнения памяти
```python
for user in session.scalars(select(User).yield_per(100)):
    process(user) # Обрабатывает по 100 записей за раз

.yield_per(count, preserve_order=True)
# preserve_order - Сохранятть порядок записей, может влиять на производительность
```


## Составные запросы
---

### JOIN
---

### Подзапросы
---

### Группировка
---

### Транзакции
---


