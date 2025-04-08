---
id: pydantic
aliases: []
tags: []
---
**Back**
    [[!Python]]

# Pydantic
---
Это библиотека для Py, предназначенная для валидации и трансформации данных.
- Валидация данных (проверка входных данных на соответствие ожидаемым типам и ограничениям)
- Трансформация данных (автоматические приведение данных к нужным типам и форматам)

## Модели
---
- Наследуются от **BaseModel**
- Каждая модель описывает набор полей, которые представляют собой структуру данных и условия для их валидации

### Описание полей
---
- Типизация (Поля в модели описываются с указанием типов)
Это обеспечивает базовую валидацию

- Использование `Field()` (Позволяет аннотировать поля с дополнительными параметрами), такими как значение по умолчпнию, ограничения и другие настройки

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    email: str = Field(..., alias='email_address')
```

### Валидация полей
---
- Минимальная валидация типов (испольщование встроенных типов *Py*)
- Использование валидаторов
    `EmailStr` (проверка email-адресов)
*Для установки расширенных валидаторов требуется установка дополнительных зависимостей*

```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
```

## Декораторы
---

### @field_validator
---
Позволяет добавлять кастомную логику валидации поля
Вызывается при создании поля и изменении модели
*Для одного поля можно создать множество проверок*
```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    age: int

    @field_validator('age')
    def check_age(cls, value):
        """Гарантирует, что возраст пользователя будет больше 18"""
        if value < 18:
            raise ValueError('Возраст должен быть больше 18 лет')
        return value

```

Можно не только проверять, но и изменять значения
```python
class User(BaseModel):
    age: int

    @field_validator('age')
    def check_age(cls, value):
        return max(value, 18) # Автоматически повышает возраст до 18

```

#### Пример сложных сценариев
---
Доступ к другим полям (например к info)
```python
@field_validator('password')
def check_password(cls, value, info):
    if len(value) < info.data.get('min_length', 8):
        raise ValueError('Пароль слишком короткий')
    return value
```

Асинхронная валидация
```python
@field_validator('email')
async def check_email_unique(cls, value):
    if await database.email_exists(value):
        raise ValueError('Email уже занят')
    return value
```

### @computed_field
---
Поле, вычисляемое на основе других данных в модели.
Его можно исопльзовать для автоматической генерации значений, а также для валидации значений

```python
from pydantic import BaseModel, computed_field

class User(BaseModel):
    name: str
    surname: str

    @computed_field
    def full_name(self) -> str | None:
        """Документация для поля"""
        # Дефолтное значение на случая если вычисления упадут
        return f"{self.name} {self.surname}" if self.name else None
```


1. Автоматическая сериализаци
При вызове .model_dump() или .model_dump_json() поле full_name будет включено в вывод
```python
user = User(name="Ivan", surname="Ivanov")
print(user.model_dump())
# {'name': 'Иван', 'surname': 'Иванов', 'full_name': 'Иван Иванов'}
```

2. Валидация и документация
Вычисляемое поле становится полноценной частью схемы:
```python
print(User.model_json_schema)
# {
#   'properties': {
#     'name': {'title': 'Name', 'type': 'string'},
#     'surname': {'title': 'Surname', 'type': 'string'},
#     'full_name': {'title': 'Full Name', 'type': 'string'}
#   },
#   'required': ['name', 'surname']
# }
```

3. Ленивые вычисления
Значения вычисляются только при обращении, а не хранятся в памяти

Актуальный пример
```python
class LDAPConfig(BaseSetting):
    LDAP_SERVER_URL: str
    LDAP_COMPANY: str

    @computed_field
    def base_dn(self) -> str:
        """DC-часть DN (которая вычисляется из URL сервера)"""

        return f"DC={self.LDAP_SERVER_URL.split('://')[-1].replace(`.`, `,DC=`)}"

    config = LDAPConfig(LDAP_SERVER_URL="ldap://company.local", LDAP_COMPANY="Компания")

    print(config.model_dump())
    {
    'LDAP_SERVER_URL': 'ldap://company.local',
    'LDAP_COMPANY': 'Компания'
    }
```

#### Когда использовать
---
Для производных данных
- Поля
- Хеши
- Форматированные строки

Для динамических настроек
- base_dn из url

Когда нужно включить поле в API-ответ


#### Когда отказаться от использования
---
- Тяжелые вычисления (так как может вызываться многократно)
- Поля, которые нужно кешировать (лучше использовать @property + кеш)


### @model_validator
---
Декоратор дл я комплексных проверок (зависящих от нескольких полей)

`@model_validator(mode='after')`
(Валидация должна выполняться после создания экземпляра модели, когда уже доступны все поля)

Сначала выполняются базовые проверки, а только потом `@model_validator(mode='after')`

```python
from pydantic import BaseModel, model_validator

class User(BaseModel):
    age: int
    has_parent_consent: bool
    country: str

    @model_validator(mode='after')
    def check_age_rules(self):
        # Проверка для США (возраст <16 требует согласия родителей)
        if self.country == "US" and self.age < 16 and not self.has_parent_consent:
            raise ValueError("Для пользователей младше 16 лет требуется согласие родителей")
        return self
```
