---
id: ACME
aliases:
  - ACME
tags: []
---
**Back**
    [[Certs]]

# ACME
---
Автоматизированная среда управления сертификатами

[[acmesh]]
[[certbot]]

1. Клиент ACME
ПО, спосощью которого пользователи решают задачи, связанне с сертификатами. Когда требуется новый сертификат, клиент создает запрос на подписание сертификата CSR и отправляет его на сервер ACME

2. Сервер ACME
Управляемый центром сетификации, обрабатывает этот запрос и выдает сертификат, когда убедится, что все в порядке


## Работа протокола
---
1. Клиенты ACME (ПО установленное на веб-сервере) - отвечают за взаимодействие с сервером ACME для управления сертификатами

2. Запрос действий по управлению сертификатами. Клиент ACME инициирует запросы на получение сертификатов или выполнение других действий, связанных с сертификатами.

3. Генерация закрытого ключа и CSR. Клиент генерирует закрытый ключ и запрос на подписание сертификата. CSR содержит информацию о домене, для которого запрашивается сертификат, и открытый ключ, соответсвующий закрытому ключу.

4. Процесс проверки домена. Процедура проверки домена гарантирует, что организация, запрашивающая сертификат, контролирует домен и авторизованную пару ключей.

5. Выпуск сертификатов. Как только домен подтвержден, сервер ACME приступает к выпуску сертификатов.

6. Безопасное HTTPS-соединение. Выпущенный сертификат устанавливается на веб-сервер, позволяя ему устанавливать безопасное HTTPS-соединение с пользователями.


## Общая настройка
---
1. Установка клиента ACME
2. Регистрации учетной записи в ЦС
3. Доказательство права собственности (например разместить файл на веб-сервере или обновить DNS-записи (txt))
4. Получение сетификата. Клент запросит и получит сертификат от центра сертификации.
5. Настройка сервера. Настройка параметров сервера, чтобы использовать новый сертификат.
6. Автоматизация. Настроить ACME на автоматическое обновление сертификата.
