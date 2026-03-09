---
id: port_forwarding
aliases:
  - Проброс портов
tags: []
---

# Проброс портов
---
IP -> Firewall -> Nat

1. Добавляем правило (пример для nginx-reverse-proxy):

*chain*: dstnat (основная цепочка для перенаправления входящих запросов)
*protocol*: TCP
*Dst. port*: 443
*In. Interface*: pppoe-out (Внешний интерфейс, который смотрит в интернет)

*Action*: dst-nat
*To Addresses*: Внутренний IP-адрес сервера
*To Ports*: 443


*chain*: dstnat (основная цепочка для перенаправления входящих запросов)
*protocol*: TCP
*Dst. port*: 80
*In. Interface*: pppoe-out (Внешний интерфейс, который смотрит в интернет)

*Action*: dst-nat
*To Addresses*: Внутренний IP-адрес сервера
*To Ports*: 80

