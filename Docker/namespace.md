# Namespace
**Namespace** в Linux - это функция ядра, позволяющая изолировать и виртуализировать глобальные системыные ресурсы множества процессов.

Пример ресурсов для виртуализации.
- PID - изоляция дерева системных процессов
- NET - изоляция сетевого стека хоста
- MNT - изоляция точек монтирования файловой системы хоста
- UTS - изоляция имени хоста
- IPC - изоляция имени хоста
- USER - изоляция утилит межпроцессного взаимодействия (сегменты разделяемой памяти, семафоры)
- CGROUP - изоляция виртуальной файловой системы cgroup хоста

## Файловая система (Mount)
Пространство имен файловой системы - это независимое дерево файловой системы, ассоциированное с определенной группой процессов.
- Каждое пространство имен предоставляет уникальный вид файловой системы для всех процессов, принадлежащих этому пространству.
- При создании новых пространств имен можно установить флаг для копирования списка точек монтирования из родительского пространства. 
  *Однако последующие операции по монтированию и размонтированию в одном пространстве никак не сказываются на других пространствах*
- Между пространствами можно установить связь *ведущий-ведомый*   
  *Тогда все действия, связанные с монтированием, в пространстве ведущего распространяются и на прсотранства, помеченные как ведомые*

## UTS Unix Time Sharing
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
Пространство имен PID изолирует пространство ID процессов
*(Процессы в различных пространствах могут иметь одинаковые ID)*

