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
git clone https://github.com/Neilpang/acme.sh.git
cd acme.sh
./acme.sh --install \
          --home ~/myacme \
          --config-home ~/myacme/data \
          --cert-home ~/mycerts \
          --accountemail "hi@acme.sh" \
          --accountkey ~/myaccount.key \
          --accountconf ~/myaccount.conf \
          --useragent "this is my client."
```

Source: [translates](https://translated.turbopages.org/proxy_u/en-ru.ru.c4c7d210-685ffc6f-47ddf9fc-74722d776562/https/www.howtoforge.com/getting-started-with-acmesh-lets-encrypt-client/)
