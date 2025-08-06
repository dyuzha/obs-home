---
id: acmes.sh
aliases:
  - acmes.sh
tags: []
---

# acmes.sh
---
Простой, мощный и удобный клиент протокола ACME
Написан на shell
Совместимый с
- bash
- dash
- sh

Помогает управлять
- установкой,
- продлением
- отзывом SSL-сертификатов

Нулевые зависимости
Не требует root-прав (но рекомендуется!)

Поддерживаемые методы проверки
- web-root
- Автономный режим
- Автономный режим tls-alpn
- Apache
- Nginx
- DNS
- Псевдоним DNS
- Без состояния


## Установка
 ---
 ```bash
curl https://get.acme.sh | sh

# или

wget -O - https://get.acme.sh | sh
source ~/.bashrc

# или

git clone https://github.com/Neilpang/acme.sh.git
cd ./acme.sh
./acme.sh --install
source ~/.bashrc
```

Программа установки выполнит 3 действия:

1. Создайте и скопируйте acme.sh в свою домашнюю папку ($HOME): `~/.acme.sh/`.
Все сертификаты также будут размещены в этой папке.
2. Создайте псевдоним для: acme.sh=`~/.acme.sh/acme.sh`.
3. Создайте ежедневное задание cron для проверки и обновления сертификатов при необходимости.


### Расширенная установка
---
``` bash
curl https://get.acme.sh | sh -s -- --install \
          --home ~/.acme.sh \
          --config-home ~/.acme.sh \
          --cert-home ~/.acme.sh \
          --accountemail "не задан" \
          --accountkey ~/.acme.sh/account.key \
          --accountconf ~/.acme.sh/account.conf \
          --useragent "acme.sh"
```


Так как acme.sh по умолчанию использует ZeroSSL, который требует привязки email
Варианты решения:
```bash
# Зарегестрировать email в ZeroSSL
acme.sh --register-account -m your@email.com

# Установить Let's Encrypt в качестве CA
acme.sh --set-default-ca --server letsencrypt

# Выпускать сертификаты БЕЗ регистрации:
acme.sh --issue --dns dns_cf -d example.com
```


## Варианты автоматизации
---
- DNS провайдер (если есть api)
- Webroot (если есть доступ к файлами сайта)
- Standalone (для тестов, для локальных сайтов) (требует [[socat]])
    Запускает встроенный web-сервер на 80 порту (или 443 для TLS)
    НЕ подходит для wildcard-сертификатов (нужен DNS-режим)

### DNS провайдер
---
```bash
# пример для wildcard-сертификата
acme.sh --issue --dns dns_cf \
          -d "example.com" \
          -d "*.example.com" \
          --keylength ec-384 \
          --staging
```



## Доп параметры
---

### Генерация
---
По умолчанию, acme.sh использует [[RSA]] ключ  (2048 символов - 4096 бит)
Чтобы использовать актуальный ключ ECC (384 бита) и снизить нагрузку на процессор, не потеряв в безопасности, необходимо указать
```bash
# Указать альтернативный способ шифрования (генерации) ключа
--keylength ec-384
```

| Category           | ECC-384                 | RSA-4096      | RSA-2048      |
|--------------------|-------------------------|---------------|---------------|
| Key-size           | 384 bit                 | 4096 bit      | 2048 bit      |
| Безопасность       | Оч. высокая             | Высокая       | Устаревающая  |
| Производительность | Fast                    | Slow          | Middle        |
| Совместимость      | Современные ОС/браузеры | Универсальная | Универсальная |




## Команды
---

| Command        | Action                                        |
|----------------|-----------------------------------------------|
| --issue        | Получить новый сертификат                     |
| --install-cert | Скопировать сертификат в нужные папки         |
| --deploy       | Использовать готовый скрипт для развертывания |


### Issue
---
```bash
# Получение сертификата
acme.sh --issue -d example.com

# Получение сертификата Nginx
acme.sh --issue -d example.com --nginx
# Для Apache
--apache

# Выпуск wildcard сертификата
acme.sh --issue -d example.com *.example.com

# Выпуск тестового сертификата
acme.sh --issue -d example.com --staging

# Выбор длины ключа
acme.sh --issue -d example.com --keylength ec-384

# Подробный вывод для диагностики
acme.sh --issue -d example.com --standalone --debug 2
```

- Выпускает новый SSL-сертификат через CA
- Проверяет владение доменом (через DNS или HTTP-запросы)
- Сохраняет сертификат в папке `/.acme.sh/domain/`


#### Генерация
---
По умолчанию, acme.sh использует [[RSA]] ключ  (2048 символов - 4096 бит)
Чтобы использовать актуальный ключ ECC (384 бита) и снизить нагрузку на процессор, не потеряв в безопасности, необходимо указать
```bash
# Указать альтернативный способ шифрования (генерации) ключа
--keylength ec-384
```

| Category           | ECC-384                 | RSA-4096      | RSA-2048      |
|--------------------|-------------------------|---------------|---------------|
| Key-size           | 384 bit                 | 4096 bit      | 2048 bit      |
| Безопасность       | Оч. высокая             | Высокая       | Устаревающая  |
| Производительность | Fast                    | Slow          | Middle        |
| Совместимость      | Современные ОС/браузеры | Универсальная | Универсальная |


#### Тестовая среда
---
```bash
# Выпустить тестовый сертификат
--staging
```

Предназначена для тестирования и отладки процессов выпуска SSL-сертификатов без рисков ПРЕВЫСИТЬ ЛИМИТЫ prod-серверов
- Используется тестовый URL
- Сертификаты выдаются под промежуточным CA (Staging), НЕ ДОВЕРЯЕМЫМ БРАУЗЕРОМ
- Лимиты
30k сертификатов на домен в неделю
60 неудачных процессов в час

После использования можно удалить тестовые сертификаты
```bash
find ~/.acme.sh/ -name "*_staging*" -exec rm -rf {} \;
```


##### Standalone
---
Необходим установленный [[socat]]
```bash
acme.sh --issue -d srv.dyuzha.ru --staging --standalone

# Результат должен быть таким
~/.acme.sh/example.com/
  ├── example.com.key     # Приватный ключ
  ├── example.com.cer     # Сертификат
  └── fullchain.cer       # Полная цепочка (сертификат + CA)
```


##### Dns
---
Возможно выпустить **wildcard** сертификаты
```bash
acme.sh --issue -d example.com -d *.example.com --staging --dns dns_provider
acme.sh --issue -d example.com -d *.paun.su --staging --dns dns_cf

# Для CloudFlare

# Предварительно должны быть экспортированы
echo 'export CF_Token="ваш_токен"' >> ~/.bashrc
echo 'export CF_Account_ID="ваш_ID"' >> ~/.bashrc
source ~/.bashrc  # Применить изменения

acme.sh --issue -d example.com --staging --dns dns_cf

```

Ручной ввод
```bash
# Показывает TXT запись которую нужно разместить
acme.sh --issue -d example.com --dns \
    --yes-I-know-dns-manual-mode-enough-go-ahead-please

# После добавления TXT записи
acme.sh --renew -d example.com \
  --yes-I-know-dns-manual-mode-enough-go-ahead-please
```


### Install-cert
---
```bash
# Установка сертификата
acme.sh --install-cert
```
- Копирует **УЖЕ ПОЛУЧЕННЫЙ СЕРТИФИКАТ** из ~/.acme.sh/ в указанные пути (например `/etc/nginx/ssl/`)
- Может выполнить команду перезагрузки сервиса (например `nginx -s reload`)

```bash
acme.sh --install-cert -d example.com \
    --key-file /etc/nginx/ssl/key.pem \
    --fullchain-file /etc/nginx/ssl/cert.pem \
    --reloadcmd "nginx -s reload"

--key-file # Путь для приватного ключа
--fullchain-file # Путь для сертификата (включая цепочку доверия)
--reloadcmd # Команда для перезагрузки сервиса

```
Вместо `--install-cert` можно использовать готовые срипты из ` ~/.acme.sh/deploy`
Это аналог `--install-cert`, но с предопределенными путями (например для nginx, apache, docker)
```bash
acme.sh --deploy -d srv.dyuzha.ru --deploy-hook nginx
```

