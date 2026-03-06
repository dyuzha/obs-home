---
id: ssh-copy-id
aliases:
  - ssh-copy-id
tags: []
---
**Back**
    [[!!Base]]

# ssh-copy-id
---
Удобный способ скопировать публичный SSH-ключ.
Позволяет подключаться на сервер без ввода пароля

1. Создание SSH-ключа
```bash
# Просмотреть доступные SSH-ключи
ls ~/.ssh/

# В случае их отсуствия

# Создать новый ключ
ssh-keygen -t ed25519 [ -C "ypu_email@example.com" ]
ssh-keygen -t ed25519 [ -C "ansible-prod@2025" ]
# -C - добавляет коментарий
#  Указывать email в качестве коментария - удобный способ идентификации
```

2. Копирование ключа на сервер
```bash
ssh-copy-id user@user_ip

ssh-copy-id root@192.168.1.10  # Для пользователя root
ssh-copy-id ubuntu@203.0.113.42  # Для пользователя ubuntu
```
