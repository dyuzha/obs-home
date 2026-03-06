---
id: werkzeug
aliases: []
tags: []
---
**Back**
    [[!Python]]

# Werkzeug
---
Пакет реализующий хеширование

## Hello word!
---
Хеширование
```python
from werkzeug.security import generate_password_hash

hash = generate_password_hash('foobar')
print(hash) # 'scrypt:32768:8:1$DdbIPADqKg2nniws$4ab051ebb6767a...'
```

Проверка
```python
from werkzeug.security import check_password_hash

result = check_password_hash(hash, 'foobar')
print(result) # True | False
```

