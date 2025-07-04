---
id: pipe
aliases:
  - Pipe
tags: []
---
**Back**
    [[!Lin]]

# Pipe
---
Конвеер - это однонаправленный канал межпроцессного взаимодействия

Чаще все используются в shell-скриптах для связи нескольких команд путем перенаправления вывода команды (**stdout**) на вход (**stdin**) последующий.
```bash
cmd1 | cmd2 | ... | cmdN
```

## Логика
---
**Конвейер** обеспечивает асинхронное выполнение команд с использованием буферизации ввода/вывода.
=> Все команды работают параллельно, каждая в своем процессе.
При попытке чтения из пустого буфера процесс чтения блокируется до появленрия данных.
При попытке записи в заполненный буфер процесс записи будет заблокирован до освобождения необходимого места.

Не смотря на то, что конвейер оперирует файловыми дескрипторами потоков ввода/вывода, все операции выполняются в памяти, без нагрузки на диск

## Cases
---
Можно перенаправить вывод скрипта в интерпритатор для выполнения первого

```bash
cat myscript.sh | sh
curl https://get.acme.sh | sh
wget -O - https://get.acme.sh | sh
```
