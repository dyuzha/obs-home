---
id: flask-migrate
aliases: []
tags: []
---
**Back**
    [[Flask]]

# Flask-Migrate
---
Flask-обертка для Alembic, основа для миграции базы данных SQLAlchemy

## Инициализация
---
```python
from flask import Flask
from flask-sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
```

Создание репозитория миграции
```bash
# Определение переменных
SQLALCHEMY_DATABASE_URI = 'sqlite:///base.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Определение моделей дб
# ...

# Создание репозитория миграции
flask db init
```

