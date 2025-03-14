---
id: namespace
aliases: []
tags: []
---

# Namespace
---
**Namespace** в Linux - это функция ядра, позволяющая изолировать и виртуализировать глобальные системыные ресурсы множества процессов.

Пространство имен обеспечивает проуессы собственным системным представлением, тем самым изолируя независимые процессы друг от друга. **Нельзя взаимодействовать с тем, что не видно**

Сильная сторона пространств имен в том, что они ограничивают доступ к системным ресурсам без информирования об этом

Пример ресурсов для виртуализации.
- PID - изоляция дерева системных процессов
- NET - изоляция сетевого стека хоста
- MNT - изоляция точек монтирования файловой системы хоста
- UTS - изоляция имени хоста
- IPC - изоляция имени хоста
- USER - изоляция утилит межпроцессного взаимодействия (сегменты разделяемой памяти, семафоры)
- CGROUP - изоляция виртуальной файловой системы cgroup хоста


## Файловая система (Mount)
---
Пространство имен файловой системы - это независимое дерево файловой системы, ассоциированное с определенной группой процессов.
- Каждое пространство имен предоставляет уникальный вид файловой системы для всех процессов, принадлежащих этому пространству.
- При создании новых пространств имен можно установить флаг для копирования списка точек монтирования из родительского пространства.
  *Однако последующие операции по монтированию и размонтированию в одном пространстве никак не сказываются на других пространствах*
- Между пространствами можно установить связь *ведущий-ведомый*
  *Тогда все действия, связанные с монтированием, в пространстве ведущего распространяются и на прсотранства, помеченные как ведомые*

## UTS Unix Time Sharing
---
Пространство имен UTS используется для изоляции двух конкретных элементов системы, относящихся к системному вызову `uname()`

Система характеризуется системным вызовом `uname()`
  возвращает структукру utsname, состоящую из 6 строк:
  - sysname
  - nodename
  - release
  - version
  - machine
  - domainname

При этом, только 2 элемента изменяются во время выполнения:
  - nodename
  - domainname

Пространство имен **UTS**  изолирует эти два системных идентификатора.

- В контейнеризации функция пространства имен **UTS** позволяет каждому контейнеру иметь свое имя хоста и имя домена.

- Для Существования нескольких экземпляров пространств имен UTS, происходит выделение новых экземпляров структуры `utsname` в ядре для каждого экземпляра такого пространства и изменение системных вызовов, которые изменяют значение пространства для поиска подходящего экземпляра структуры `utsname` в качестве текущего.

## PID
---
Пространство имен PID изолирует пространство ID процессов
*(Процессы в различных пространствах могут иметь одинаковые ID)*
- В новом пространстве имен первый проуесс является иниуиализирующим (init-процессом) PID = 1
- По завершению init-процесса ядро завершает все процессы, принадлежащие одному пространствк через сигнал `SIGKILL`.

## Network (Сети)
---
Пространство имен для сетей предостваляет изоляцию систем ресурсов связанных с сетями:
- сетевое оборудование
- стеки протоколов IPv4 и IPv6
- таблицы маршрутизауии
- файрволы
- номера портов (socets)
- тд

Физические сетевые устройства могут принадлежать только одному пространству.
Каждое пространство имен может иметь одно или несколько виртуальных устройств
  Для обеспечения доступа во внешнюю сеть между физическим и виртуальнвм устройством из разных пространств создается мост.

Когда последний процесс в пространстве завершается, то физическое сетевое устройство возвращается не в родительское пространство, а в пространство хостовой машины.

## Межпроцессное взаимодействие (IPC)
---
(HINT) - для других пространств
**System V IPC** включает в себя
- (???) семафоры
- (???) разделяемую память
- (???) очереди сообщений

Каждый ресурс межпроцессного взаимодействия должен иметь свой уникальный идентификатор (ID).
 -> Это позволяет процессам, взаимодействующим между собой, обращаться к общему ресурсу. ->
 -> Для изоляции таких ресурсов было создано пространство имен IPC

Каждое пространство имен IPC имеет свои собстенные наборы
- набор идентификаторов System V IPC
- набор очередей сообщений POSIX

Объекты, созданные в этом пространстве имен, видны всем процессам, состоящим этом пространстве, и не видны всем остальным процессам в других пространствах имен

- Новое протсранство имен создается без копирования
- Последний процесс в этом пространстве завершается ->
-> пространство имен IPC разрушается ->
-> Все объекты уничтожаются

## Пользовательские ID (User)
---
Пространство имен пользователей изолируют
- ID пользоватеоей
- ID групп
- корневой каталог
- ключи
- capabilities

**Идентификаторы пользователя** и **группы процесса** могут отличаться внутри и вне пространства имен пользователей.

Например процесс вне пространство имен мб не привилигированным, а в пространстве имен - привиллигированным

Пространство имен могут быть вложенными =>
=> Каждое пространство имен пользователей (кроме init-пространства) имеет родительское пространство и может иметь 0 и более дочериних пространств.

Ядро накладывает лимит в 32 вложенных уровня пространств имен пользователей

## Контрольные группы (Cgroup)
---
Пространство имен cgroup скрывает к какой группе принадлежит процесс. В таком пространстве имен процесс,  проверяя к какой группе он относится, увидит путь относительно контрольной группу, установленной при создании.

- Процесс считает, что принадлежит к корневой контрольной группе
- Полный путь к кнонтрольной группе скрыт

## Время
---
Пространство имен времени позволяет процессам видеть различное системное время
-> Подобно тому, как пространство имен UTS изолирует имя хоста.

