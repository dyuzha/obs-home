---
id: sqlalchemy
aliases:
  - SQLAlchemy
tags: []
---
**Back**
    [[!Python]]

**More**
    [[sa_relationship]]
    [[sa_select]]
    [[sa_subqueries]]
    [[sq_where_filter]]
    [[sa_identity_map]]


# SQLAlchemy
---
Библиотека для работы с базами данных
Имеет 2 основных способы взаимодействия с бд:
- SQLAlchemy Core ("Традиционные" SQL-запросы)
- SQLAlchemy ORM (Объектно-ориентированный стиль)


## 1. SQLAlchemy Core
---
"Традиционные" SQL-запросы с синтаксисом на Python
Особенности:
- Использует таблицы (Table), а не классы моделей
- Запросы строятся через select(), insert(), update(), delete()
- Фильтрация через where()
- Нет привязки к объектам - возвращаются строки, кортежи, словари

> [!Example]
```python
from sqlalchemy import select, table, column

users = table('users', column('id'), column('name'))
# SQL-statement (инструкция)
stmt = select(users).where(users.c.name == 'Alice')
result = connection.execute(stmt).fetchall()
```
- Полный контроль над SQL
- Высокая производительность для сложных запросов
- Подходит для аналитики и массовых операций


## 2. SQLAlchemy ORM
---
Высокоуровневый подход, где изменены привычные представления
- Классы - Таблицы
- Объекты - Строки

Особенности:
- Использует модели (классы, наследующие Base)
- Запросы через session.query(Model) или session.execute(select(...)) *в новых версиях*
- Фильтрация через .filter() *В старом стиле*, .where() *В новом стиле*
- Результаты - объекты моделей, а не сырые данные
> [!Example]
```python
froom sqlalchemy.orm import Session

# Старый стиль представления объектов
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

# Старый стиль
users = session.query(User).filter(User.name == 'Alice').all()

# Новый стиль
stmt = select(User).where(User.name == "Alice")
users = session.execute(stmt).scalars().all()
```
- Удобствтво работы с объектами
- Автоматическая загрузка связей
- Подходит для бизнес-логики приложений

### Новый стиль представления объектов
---
Начиная с 2.0, рекомендуется исопльзовать аннотации типов (Как в Pydantic/FastAPI) с `mapped_column`

```python
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__="users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
```
- Лучшая интеграция с системами типизации (mypy, IDE)
- Более читаемый код (особенно для большиъ моделей)
- Поддержка новых возможностей SQLAlchemy 2.0

**Важные изменения в SQLAlchemy 2.0**
- `declarative_base()` устарел в пользу `DeclarativeBase`.
- `Column` заменяется на `mapped_column` (но остаётся для обратной совместимости).
- Аннотации `Mapped[]` стали стандартом для типизации.



## Выполнение Core запросов через session
---
Вместо `connection.execute()`, можно использовать `session.execute()`

Плюсы:
- Единый интерфейс (`session`) для ORM и Core
- Возможность смешивать ORM-модели и Core-таблицы в одном запросе
- Управление транзакциями через `session.commit()`

Минусы:
- Некоторые Core-операции (например, DDL - создание таблиц), удобнее делать через `connection`
- В ORM-сессии есть кэш (identity map) , который может влиять на производительность при массовых операциях (см. [[sa_identity_map]])
