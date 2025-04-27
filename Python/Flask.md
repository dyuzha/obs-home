---
id: Flask
aliases: []
tags: []
---
**Back**
    [[!Python]]

# Flask
---
[[flask-sqlalchemy]]
[[flask-migrate]]
[[flask-wtf]]
[[flask-login]]

### Создание бд
---
```python
from file import app, db
app.app_context().push()
db.create_all()
```
- В результате создаться папка instance *(там будет бд)*

# Flask
---
- компактный фреймворк для быстрой разработки веб-приложений.
Он предоставляет минимальную необходимую функциональность и не навязывает никаких строгих правил в отношении структуры и архитектуры
- На фласк легко реализовать генератор статических сайтов


## Hello Word
---
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
  def hello():
    return 'Hello, World'

if __name__ == '__main__':
  app.run()
```

## Основные команды
---

### run
---

### shell
---
Запускает интерпритатор **Py**, в контексте приложения
```bash
flask shell
# Запускает интерпритатор
# Импортирует app и другие объекты (которые натсроены)
```

```python
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post

# Настройка контекста оболочки
@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}
```

