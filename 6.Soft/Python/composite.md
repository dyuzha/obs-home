---
id: composite
aliases: []
tags: []
---
**Back**
    [[!Python]]


# Композиция
---
Подход при котором объект содержит другие объекты в качестве своих полей (атрибутов) и делегирует им часть свой функциональности

## Пример композиции
---
```python
class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class JSONSerializer:
    def to_json(self, data):
        import json
        return json.dumps(data)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.logger = Logger()  # Композиция: User содержит Logger
        self.serializer = JSONSerializer()  # Композиция: User содержит JSONSerializer

    def log_info(self):
        self.logger.log(f"User: {self.name}, Age: {self.age}")

    def to_json(self):
        return self.serializer.to_json({"name": self.name, "age": self.age})

# Использование
user = User("Alice", 25)
user.log_info()  # [LOG] User: Alice, Age: 25
print(user.to_json())  # {"name": "Alice", "age": 25}
```
