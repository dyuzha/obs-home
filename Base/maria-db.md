---
id: maria-db
aliases:
  - maria-db
tags: []
---
**Back**
    [[!Base]]

# maria-db
---

Релиационная система управления бд (Форк MySQL)

```bash
# Утилита для базовой настройки безопасности
mysql_secure_installation

# Проверка конфигурационного файла
mysqld --validate-config
```

Основной конфигурационный файл:
`/etc/mysql/my.cnf` или `/etc/my.cnf` или `/etc/mysql/mariadb.conf.d`

Модульная система конфигураций, конфигурационные файлы запускаются в алфавитном порядке из `mariadb.conf.d/`

a2enmod (Apache 2 ENable MODule)
- активирует модуль mod_rewrite
 ,который отвечает за:

Основное назначение модуля mod_rewrite:
- Перенаправление URL (редиректы)
- Например, с http на https или с старого URL на новый.
- ЧПУ (человеко-понятные URL)
- Преобразует example.com/?p=123 → example.com/my-post.
- Защита от горячих ссылок (hotlink protection)
- Блокирует воровство вашего контента (картинок, видео).
- Управление доступом
- Запрет доступа к скрытым файлам (например, .htaccess).

После выполнения:

Создается симлинк из /etc/apache2/mods-available/rewrite.load → /etc/apache2/mods-enabled/rewrite.load.

Apache получает доступ к функционалу перезаписи URL.
