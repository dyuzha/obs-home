---
id: Flask
aliases: []
tags: []
---
**Back**
    [[!Python]]

# Flask
---

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
Он предоставляет минимальную необходимую функциональность и не навязывает никаких строгих правил ы отношении структуры и архитектуры
- На фласк легко реализовать генератор статических сайтов


# Install
---
```bash
python -m venv flaskenv

source flaskenv/bin/python/activate

pip install flask
```

# Hello Word
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

