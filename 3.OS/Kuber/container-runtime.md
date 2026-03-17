---
id: container-runtime
aliases:
  - Container-runtime
tags: []
---


# Container-runtime
---
Программа управления контейнерами на ноде
- Запускает, останавливает, создает, удаляет контейнеры
- Взаимодействует с образами (pull/push)
- Изолирует контейнеры через `namespaces` и `cgroups`

containerd
CRI-O - опртимизирован для Kubernetes (использует runc)
Docker - устаревший

Использует (создает pod sandbox):
- cgroups - лимиты CPU/памяти
- namespaces - сеть, PID, filesystem
- overlayFS / storage - для файловой системы контейнера


