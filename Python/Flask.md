# Создание базы данных

```python
from file import app, db
app.app_context().push()
db.create_all()
```
- В результате создаться папка instance *(там будет бд)*
