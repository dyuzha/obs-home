---
id: ssh
aliases:
  - SSH
tags: []
---
**Back**
    [[!Lin]]

# SSH
---


## ssh-keygen
---
```bash
# Сгенерировать ключ с шифрованием ed25519
# -С это комментарий (в данном случае email)
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

ssh-keygen -t ed25519 -C "comment"

# Более надежный ключ
ssh-keygen -t ed25519 -o -a 100 -C "comment"
-o # более стойкий формат ключа
-a 100 # Увеличить количество раундов хеширования
```

*Ed25519 (наиболее современный и безопасный)*
*RSA 4096 бит (если нужна максимальная совместимость)*


## ssh-copy-id
---
```bash
# Скопировать публичный ключ на удаленный host
ssh-copy-id <server> # Возьмет файл из пути по умолчанию

# Скопировать конкретный публичный ключ на удаленный host
ssh-copy-id -i <path/to/file.key.pub> <server>
```
