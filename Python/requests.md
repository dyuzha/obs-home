Back
[[modules.md]]

# Requests
---
**Requests** - Библиотека для выполнения HTTP-запросов на языке **Py**
Она создана для
- упрощения взаимодействия с API и веб-ссервисами,
- получения данных с веб-сайтов
- выполнения других задач на основе HTTP

## Методы
---
`GET` - Обычный запрос к серверу, для получения информации по URL
`POST` - Запрос с данными в теле запроса


`PUT` - Заменяет существующий объект на полностью новый
`DELETE` - Удаляет объект сервера
`HEAD` - Запрашивает ответ, идентичный запросу `GET` **Но без тела отвтеа**
`PATCH` - Частично обновляет существующий объект

## Ошибки
---
**405** - Method Not Allowed
Ресурс не поддерживает такой ресурс


## GET
---
`rq.get( 'URL-адрес', {key: value}, ... )`

```python
google_link = "https://google.com"
getParams = {'param1': 'value1', 'param2': 'value2'}
response = rq.get(google_link, getParams)

print(response.url)
# https://www.google.com/?param1=value1&param2=value2
```

## POST
---
`rq.post( 'URL-адрес', {key: value}, ... )`

```python
test_link = "https://httpbin.org/post"

postparams = {'param1': 'value1', 'param2': 'value2'}
response = rq.post(test_link, postparams, timeout=2)

print(response.json()['form'])
#>>>{'param1': 'value1', 'param2': 'value2'}
```


## OPTIONS
---
- Какие запросы поддерживает ресурс


