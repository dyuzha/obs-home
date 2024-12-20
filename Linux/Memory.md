# Память в Linux
---

## Управление памятью для процессов
---
Любой запущенный процесс получает собственный выделенный участок памяти.
НО этому процессу не доступны физические адреса

-> Процесс использует *Виртуальное адресное пространство*, являющимся дополнительным слоем абстракции между процессом и физической памятью.

Для сопоставления адресов между виртуальной и физической памятью, используется специальные структуры - *таблицы страниц*

### Преимущества
---
1. Изоляция процессов друг от друга
  *Каждый из них работает в собственном виртуальном пространстве и не имеет доступа к памяти других процессов.*

2. Гибкое управление памятью для системы
  *Например, для неактивного процесса часть страниц мб перенесено из оператиыной памяти в пространство подкачки, но этот никак не повлияет на работу самого процесса*
    - Адресное пространство не измениться
    - Измениться лишь трансляция в таблице страниц

3. Позволяет экономить физическую память
  *Если несколько процессов используют одни и те же данные, то система может транслировать адреса виртуальных пространств на один и тотже участок физической памяти*

**Итого**:
  Размер виртуальной памяти в системе теоретически ничем не ограничен
  - ее общий объем может существенно превышать имеющуюся в наличии физическую память

**Например**:
  Запущенно несколько графических приложений Qt и GTK
  - Достаточно 1 раз загрузить библиотеку в память, а затем просто транслировать адреса виртуальной памяти процессов на одни и теже участки физической памяти  

  - При этом каждый процесс будет думать, что у него загружена собственная копия библиотек

Поэтому  современные Linux-системы выделяют память процессам с превышением имеющейся в наличии физической памяти (RAM + Swap)

### OOM-Killer
---
Случается, что процессы съедают всю доступную физическую память и вот тут системе надо выбрать что-то дно.
  - Убить один из процессов (Используется OOM-Killer)
  - Вызвать Kernel panic

OOM-Killer используется в современных системах по умолчанию

- Использует достаточно сложный анализ и присваивает каждому процессу очки негодности (badness)
- Диапазон очков `[-1000; 1000]`
  - Чем выше процесс тем больше шансов на убийство
  - -1000 никогда будет убит OOM-Killer

Как вычисляются очки негодности
  - За основу берется процент физической памяти, используемый процессом и умножается на 10
  - 100% это 1000
  Затем применяются различные модификаторы к данному значению
    - Прибавляется половина очков всех дочерних процессов, имеющих собственную виртуальную память
    
    - Если приоритет процеса больше нуля очки умножаются на 2

    - Очки делятся на коэфф., связанный с процессорным временем, чем более активен процесс и чем больше процессорного времени он использует, тем больше будет этот коэффицент
    - ...

OOM-Killer - убивает самый "толстый" процесс, который наименее активен в системе и имеет самое короткое время жизни.
Такой подход позволяет достаточноточно бороться с утечками памяти

```bash
# Вывести количество очков, присвоенных процессов
cat /proc/PID/oom_score

# Изменить  количество очков исполдбзуя коэфф. oom_adj
echo -17 > /proc/PID/oom_adj
# Отправили процессу PID значение -17, т.е. обеспечили полную защиту от OOM-Killer
```

Выше приведенные операции имеют недостатки:
- Это необходимо делать в ручную (максимум скрипт)
- Действие необходимо применять к запущенным процессам

В современных системах для управления службами используется `systemd`, который предосстовляет простые и эффективные инструменты для управления очками негодности.
Для этого в секцию `[Service]` юнита службы необходимо добавить опцию
```bash
[Service]

OOMScoreAdjust=-500
```
- `OOMScoreAdjust` показывает на сколько следует изменить количество очков процесса относительно рассчитанного количества, в нашем примере мы уменьшили его на 500.


source: [Что такое OOM-Killer и как он работает](https://interface31.ru/tech_it/2022/09/linux---nachinayushhim-chto-takoe-oom-killer-i-kak-on-rabotaet.html)