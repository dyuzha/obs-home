---
id: htpasswd
aliases:
  - htpasswd
tags: []
---
**Back**
    [[!!Base]]

# htpasswd
---
Утилита командной строки, используемая для создания и управления файлами паролей, которые применяются для базовой аутентификации HTTP (HTTP Basic Authentication) на веб-серверах, таких как Apache и  Nginx

Файл `.htpasswd` хранит логины и хешированные пароли пользователей, которым разрешен доступ к защищеннам директориям веб-сервера

## Основные команды
---
```bash
# Создание нового файла с перым пользователем
htpasswd -c /path/to/.htpasswd username

# Добавление нового пользователя в существующий файл
# Без -c чтобы не перезаписать файл
htpasswd /path/to/.htpasswd username

# Удаление пользователя
htpasswd -D /path/to/.htpasswd username

# Проверка пароля
htpasswd -v /path/to/.htpasswd username
```

## Формат файла
---
```bash
login:hash_pass

user1:$apr1$XUoHhL4y$S3N6DvDz5UQ5E5Q9oLq1H/
user2:$apr1$sE4iKk4W$TqZ2QoX1rY0CvF2RvW3Bx.
```


