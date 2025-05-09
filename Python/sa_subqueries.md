---
id: sa_subqueries
aliases:
  - sa_subqueries
  - Подзапросы
tags: []
---

# Подзапросы
---
- это SQL-запросы, вложенные в другие запросы
Создаются с помощью
- subquery()
- alias()

Используются в
- Фильтрации (`WHERE`, `HAVING`)
- Сравнениях (`IN`, `EXISTS`)
- Джойнах (подзапрос как временная таблица)
- Агрегации (расчеты внутри подзапроса)

## Cases
---

### Найти всех пользователей, у которых возраст больше среднего
---

#### subquery()
---
```python
from sqlalchemy import select, func

# Позапрос: вычисляется средний возвраст
avg_age_subq = selelct(fun.avg(User.age)).scalar_subquery()

# Основной запрос: находятся пользователя, у которых возраст больше среднего
users = session.query(User).filter(User.age > avg_age_subq).all()

```

