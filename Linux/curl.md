---
id: curl
aliases:
  - cURL
tags: []
---
*Back*
    [[!Lin]]

# cURL
---
**cURL** - Client URL
Программное обеспечение, которое предоставляет:
- Библиотеку **libcurl**
- Иснтрумент CLI `curl`

-- Инструмент для передачи данных с сервера или на него, спомощью протоколов
-- "Швейцарский нож" для работы с сетевыми запросами

> [!WARNING] Не сохраняет файлы автоматически, а перенаправляет их в stdout
```bash
# Скачать файл и сохранить под оригинальным именем
curl -O https://testdomain.com/testfile.tar.gz

# Скачать под другим именем
curl -o custom_file.tar.gz https://testdomain.com/testfile.tar.gz

# Скачать несколько файлов
curl -O https://testdomain.com/testfile.tar.gz -O https://testdomain.com/testfile2.tar.gz

```

## Применение curl
---
- Доступ без браузера
- Внутри **shell**-скриптов
- Для тестирования **API**
- Отслеживание-запросов

## Опции
---

### Основные

| Opt                | Description                                           |
|--------------------|-------------------------------------------------------|
| -o `<file>`        | Сохранить вывод в файл                                |
| -O                 | Сохранить вывод в файл с оригинальным названием       |
| -C -               | Продолжить прерванную загрузку                        |
| -L                 | Следовать редиректам (Если сервер возвращает 301/302) |
| --limit-rate 1M    | Ограничение скорости                                  |
| -d `<data>`        | Отправить данные для POST/PUT                         |
| -H "Header: Value" | Добавить HTTP-заголовок                               |
| -F "name=content"  | Отправить файл или форму multipart/form-data          |
| -G                 | Добавление параметров в URL (для GET)                 |


### Отлпдка и информация

| Opt | Description                                |
|-----|--------------------------------------------|
| -v  | Подробной вывод (verbose)                  |
| -s  | Тихий режим (без прогресс бара и ошибок)   |
| -S  | Тихий режим (без прогресс бара) c ошибками |
| -I  | Показывает только заголовки ответа         |


### Безопасность (SSL/TLS)

| Opt             | Description                           |
|-----------------|---------------------------------------|
| -x srv:port     | Использование http прокси             |
| -k              | Игнорировать проверку SSL-сертификата |
| --cert cert.pem | Указать клиентский SSL-сертификат     |
| --cacert ca.pem | Указать ca-сертификаты                |


### Персонализация
| Opt               | Description              |
|-------------------|--------------------------|
| -u user:pass       | Загрузка с авторизацией                               |
| -b "cookie=value" | Отправить cookie         |
| -c cookies.txt    | Сохранить cookies в файл |


## Cases
---
```bash
# 1. Выполнит обычный get-запрос
curl www.google.com

# 2. Получение заголовков HTTP(S)
curl -I https://www.google.com
curl -i https://www.google.com
curl -head https://www.google.com

# 3. Игнорирование ошибки неправильных или самоподписанных сертификатов
curl -k https://localhost/my_test_endpoint
curl --insecure https://localhost/my_test_endpoint

# 4. Отправка POST-запроса
# (key=value)
curl --data "param1=test1&param2=test2" http://test.com
# JSON
curl --data '{"param1":"test1","param2":"test2"}' \http://www.test.com

# 5. Указание типа запроса
# По умолчанию curl выполняет HTTP GET запрос
curl -X 'PUT' -d '{"param1":"test1", "param2":"test3}' \http://test.com/1
curl --request 'PUT' -d '{"param1":"test1", "param2":"test3}' \http://test.com/1

# 6. Использование авторизации
# curl -u <user:password> https://my-test-api.com/endpoint1
curl -u admin1:admin123 https://ipa-server
curl --user admin1:admin123 https://ipa-server
```

### 7. Управление резольвом имен
---
При тестировании API и перенаправлении запроса на тестовую машину, это можно сделать указав альтернативный резольв имени эндпоинта для данного запроса
Работает эквивалентно прописыванию хоста в /etc/hosts
```bash
curl --resolve www.test.com:80:localhost http://www.test.com/
```

### 8. Загрузка файлов
---
`curl -F` эмулирует отправку заполненной формы, когда пользователь нажимает кнопку отправки.
Указывает `curl` передавать данные ввиде POST-запроса, используя multipart/form-data Content-Type
```bash
# Загрузить файл
curl -F @field_name=@path/to/local_file

# Загрузить несколько файлов
curl -F @field_name=@path/to/local_file
-F @field_name=@path/to/local_file
```

### 9. Измерение продолжительности соединения
---
`-w` передает информацию в stdout после завершения передачи
Поддерживает отображение набора переменных.
- Это удобно если необходимо определить общее время скачивания с помощью `curl`
```bash
# Общее время, которое потребовалось для успешного выполнения запроса
curl -w "%{time_total}\n" -o /dev/null -s www.test.com
```


source: [cloud-vk](https://cloud.vk.com/blog/10-komand-curl-kotorye-vam-sleduet-znat/)
