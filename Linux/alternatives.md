---
id: alternatives.log
aliases:
  - alternatives.log
tags: []
---

# alternatives.log
---
Это лог файл, записывающий изменения, сделанные утилитой update-alternatives.
`update-alternatives` - утилита управляет символическими ссылками для определения команд по умолчанию
(например выбор между python2 и python3, gcc и clang)

Расположение - `/var/log/alternatives.log`

- Установка, удаление и изменение альтернатив
- Какая команда выбрана по умолчанию
- Кто и когда внес изменения (если команда выполнялася через `sudo`)
