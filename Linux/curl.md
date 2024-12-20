# cURL
---
**cURL** - Client URL
Программное обеспечение, которое предоставляет:
- Библиотеку **libcurl**
- Иснтрумент CLI `curl`

**cURL** - Инструмент для передачи данных с сервера или на него, спомощью протоколов

## Варианты применения:
---
- Доступ без браузера
- Внутри **shell**-скриптов
- Для тестирования **API**

### 1. Получить содержание страницы HTTP(S)
---

```bash
# Выполнит обычный get-запрос
curl www.google.com

# Скачать файл и сохранить под оригинальным именем
curl -O https://testdomain.com/testfile.tar.gz

# Скачать под другим именем
curl -o custom_file.tar.gz https://testdomain.com/testfile.tar.gz

# Скачать несколько файлов
curl -O https://testdomain.com/testfile.tar.gz -O https://testdomain.com/testfile2.tar.gz
```

### 2. Получение заголовков HTTP(S)
---

```bash
curl -I https://www.google.com
curl -i https://www.google.com
curl -head https://www.google.com
```

### 3. Игнорирование ошибки неправильных или самоподписанных сертификатов
---
При тестировании веб-приложений или API? в тестовом окружении могут быть самоподписанные или неправильные SSL-сетификаты.
- Deffault curl верифицирует все сертификаты.
- Что бы он не выдавал ошибку о неверных сертификатах и устаналивал соединение для тестирования, используются опции
`-k` или `--insecure`

```bash
curl -k https://localhost/my_test_endpoint
```

###4. Отправка POST-запроса
---
`-d` или `--data`

```bash
# Key=value
curl --data "param1=test1&param2=test2" http://test.com

# JSON
curl --data '{"param1":"test1","param2":"test2"}' \http://www.test.com
```

### 5. Указание типа запроса
---
По умолчанию `curl` выполняет HTTP GET запрос
- Если необходимо обновить данные, а не пересоздать их заново, то необходимо указать опцию для, указывающюю тип запроса
`-x` или `--request`
```bash
curl -X 'PUT' -d '{"param1":"test1", "param2":"test3}' \http://test.com/1
```

### 6. Использование авторизации
---
API защищено авторизацией по логину-паролю.
Можно передать пару логин-пароль, используя параметр `-u` или `--user`
```bash
curl -u <user:password> https://my-test-api.com/endpoint1
curl -u admin1:admin123 https://ipa-server
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
