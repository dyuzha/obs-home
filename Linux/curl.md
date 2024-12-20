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

1. Получить содержание страницы HTTP(S)

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

2. Получение заголовков HTTP(S)

```bash
curl -I https://www.google.com
curl -i https://www.google.com
curl -head https://www.google.com
```

3. Игнорирование ошибки неправильных или самоподписанных сертификатов

При тестировании веб-приложений или API? в тестовом окружении могут быть самоподписанные или неправильные SSL-сетификаты.
- Deffault curl верифицирует все сертификаты.
- Что бы он не выдавал ошибку о неверных сертификатах и устаналивал соединение для тестирования, используются опции
`-k` или `-insecure`

```bash
curl -k https://localhost/my_test_endpoint
```

4. Отправка POST-запроса

`-d` или `--data`

```bash
# Key=value
curl --data "param1=test1&param2=test2" http://test.com

# JSON
curl --data '{"param1":"test1","param2":"test2"}' \http://www.test.com
```

5. Указание типа запроса

```bash

```


source: [cloud-vk](https://cloud.vk.com/blog/10-komand-curl-kotorye-vam-sleduet-znat/)
