---
id: sa_relationship
aliases: []
tags: []
---
**Back**
    [[sqlalchemy]]

# Связи между таблицами
---
Связь многие ко многим осуществляется благодаря дополнительной ассоциативной таблице

Пример связи многие ко многим между 2-мя таблицами Users
```python
import SQLAlchemy as sa
import SQLAlchemy.orm as so


followers = sa.Table(
    "followers", # Имя таблицы
    db.metadata, # Тут должна быть метадата (то где SQLAlchemy хранит всю информацию о таблице), в данном контексте это db.metadata из flask
    sa.Column('follower_id', sa.Integer, sa.ForeignKey('user.id'),
        primary_key=True),
    sa.Column('followed_id', sa.Integer, sa.ForeignKey('user.id'),
        primary_key=True)
)


# 1-ый вариант с явным указанием двусторонней связи
class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
    # ...

    following: so.WriteOnlyMapped['User'] = so.relationship(
        # Настраивает таблицу ассоциаций (мост между моделями)
        secondary=followers,
        # Условие, которое связывает объект, с этой таблицей
        primaryjoin=(followers.c.follower_id == id),
        # Условие, которое связывает ассоциативную таблицу c целевым объектом
        secondaryjoin=(followers.c.followed_id == id),
        # Явная двустороняя связь (ссылка на обратное отношение)
        back_populates='followers')

    followers: so.WriteOnlyMapped['User'] = so.relationship(
        secondary=followers,
        primaryjoin=(followers.c.followed_id == id),
        secondaryjoin=(followers.c.follower_id == id),
        back_populates='following')

# 2-ый вариант с НЕявным указанием двусторонней связи
class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
    # ...

    # Определяется отношение только к backref
    following: so.WriteOnlyMapped['User'] = so.relationship(
        secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        # НЕявная двустороняя связь (ссылка на обратное отношение)

        # Устаревший метод
        backref='followers') # Автоматически создает обратное отношение

        # Современный метод, можно добавить динамическую загрузку
        backref=backref("followers", lazy="dynamic")


    # Отношение followers объявлять не нужно!
```

## 1. back_populates
---
Явная двустороння связь
- Позволяет синхронизировать изменения в таблице. То есть, если *User-1* followed для *User-2*, то, *User-2*, станет автоматически folowers, для *User-1*
- Изменения синхронизируются в обе стороны
Используется:
- Если нужно кастомизировать обратное отношение
(*например добавить lazy="dynamic"*)
P.s. В SQLAlchemy 2.0> исопльзуется relationship.backref, где можно указать доп параметры
- Для сложных моделей, где важна явность


## 2. backref
---
Неявная двустороняя связь
- Автоматически создает обратное отношение в связной модели без явного объявления (*удобен для сокращения кода*)
Используется:
- Чтобы избежать дублирование кода


### Параметры backref

#### lazy
---
стратегия загрузки

| Value    | Description                                             |
|----------|---------------------------------------------------------|
| select   | (Opt) Загружает все объекты сразу при обращении         |
| dynamic  | Возвращает запрос Query, который можно доп. фильтровать |
| joined   | Загружает связь сразу через JOIN                        |
| subquery | Использует подзапрос для загрузки                       |
| raise    | Запрещает ленивую загрузку, только явный запрос         |

Примеры:

> [!Example] dynamic
```python
# Получаем query вместо списка
followers_query = user1.followers

# Можно добавить доп. фильтры
active_followers = followers_query.filter(User.is_active == True).all()
```

#### uselist (bool)
---
Тип коллекции

- True (Opt), отношение возвращает список
- False, возврващает один объект (для 1:1)
```python
backref=backref("profile", uselist=False)  # Для отношения 1:1
```

#### cascade
---
Каскадные операции
Определяет, какие операции автоматически применяются к связным объектам
```python
backref=backref(
    "posts",
    cascade="all, delete-orphan" # Удаляет посты при удалении пользователя
)
```
- merge
- save-update (Opt)
- expunge
- delete
- delete-orphan
- all (Все кроме delete-orphan)

#### overlaps
---
Разрешение конфликтов
Используется, если несколько отношений ссылаются на одну таблицу
```python
backref=backref("managers", overlaps="employees")
```

#### remote_side
---
Для самоссылающихся отношений
```python
backref=backref(
    "parent",
    remote_side="Category.id"  # Для иерархии категорий
)
```

