---
id: fithes
aliases: []
tags: []
---

**Back**
    [[!Python]]

# Fithes
---


## Ленивая загрузка
---
- Избежание циклических импортов

```python
class JSONSerializeMixin:
    def to_json(self):
        import json  # Ленивая загрузка
        return json.dumps(self.__dict__)
```

## Кеширование
---
- Тяжелый модуль, который редко используется

```python
class JSONSerializeMixin:
    def to_json(self):
        import json
        self._json_module = json  # Кешируем модуль
        return self._json_module.dumps(self.__dict__)
```
