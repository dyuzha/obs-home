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

