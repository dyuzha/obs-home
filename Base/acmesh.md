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
source ~/.bashrc

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
- Standalone (для тестов, для локальных сайтов)

### DNS провайдер
---
```bash
# Пример для wildcard-сертификата
acme.sh --issue --dns dns_cf \
          -d "example.com" \
          -d "*.example.com" \
          --keylength ec-384
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


### Тестовая среда
---
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


Source: [translates](https://translated.turbopages.org/proxy_u/en-ru.ru.c4c7d210-685ffc6f-47ddf9fc-74722d776562/https/www.howtoforge.com/getting-started-with-acmesh-lets-encrypt-client/)
