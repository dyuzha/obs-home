---
id: ssh
aliases:
  - SSH
tags:
  - Port 22
---

**Back**
    [[!!Base]]

# SSH
---
Сетевой протокол прикладного уровня, предназначенный для безопасного кроссплатформенного удаленного доступа к системам.

Создан в качестве замены не зашифрованному *Telnet*

## SSH Server
---
Проверяет соединение одним из способов:
- По IP клиента (не слишком безопасно из-за риска подмены)
- По паре ключей (закрытый/приватный и открытый/публичный)
- По паролю клиента (передается в зашифрованном виде)

Примеры ssh-server'ов:
| OS      | Servers                              |
|---------|--------------------------------------|
| BSD     | OpenSSH                              |
| Linux   | Dropbear, LSH-server, Openssh-server |
| Windows | FreeSSHd, Copssh, WinSSHD, OpenSSH   |

## SSH Client
---
Примеры ssh-клентов:
| OS        | Servers                             |
|-----------|-------------------------------------|
| Unix-like | OpenSSH-client, putty, ssh, Vinagre |
| Windows   | Putty, SecureCRT, ShellGuard        |
| Android   | connectBot                          |

