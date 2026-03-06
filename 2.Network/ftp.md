---
id: ftp
aliases:
  - ftp
  - FTP
tags: []
---
**Back**
    [[!Base]]

# FTP
---
File Transport Protocol

## Curlftpfs
---
```bash
# Установка
apt install curlftpfs # На wsl нет

# Монтирование папки
curlftpfs user:pass@ftp.examle.ru ~/path/to/mount
```

## Lftp
---
FTP клиент для линукс
```bash
# Установка
sudo apt install lftp

# Копирования папки
lftp -e "mirror --parallel=5 /remote_folder /local_folder; quit" ftp://user:password@example.com
```

```bash
# Интерактивный режим
lftp ftp://user:password@example.com

lftp - e "команды в интерактивном режиме" ftp://user:password@example.com
```
