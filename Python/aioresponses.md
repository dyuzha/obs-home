---
id: aioresponses
aliases:
  - aioresponses
tags: []
---

# aioresponses
---
Модуль для мокинга HTTP-запросов
Нужен для тестирования асинхронного кода, в котором выполняются HTTP запросы, без реального обращения к сети.

```python
from aioresponses import aioresponses

async def test_something():
    with aioresponses() as m:
        m.get("https://api.example.com/data", payload={"result": "ok"}, status=200)

        async with aiohttp.ClientSession() as session:
            resp = await session.get("https://api.example.com/data")
            data = await resp.json()
            assert data["result"] == "ok"
```


Если ты мокуешь URL, передавай его точно (можно использовать yarl.URL(...)).
Работает только с aiohttp. Для httpx есть отдельные инструменты.
При сложных URL-ах (params, query) лучше использовать regex=True или match_querystring=True.
