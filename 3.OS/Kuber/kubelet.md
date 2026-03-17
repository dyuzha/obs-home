---
id: kubelet
aliases:
  - Kubelet
tags: []
---

# Kubelet
---
Агент на ноде


## Принцип работы
---

- Взаимодействует с CRI
Запускает поды
Следит за состоянием

- Взаимодействует с OS
Следит за состоянием ноды (CPU, RAM, Storage, FS's)
Управляет cgrooups и namespace для Pod'ов на этапе подготовки (pod sandbox)
(CRI runtime создает контейнеры внутри этих cgroups, но kubelet контролирует лимиты)

- Взаимодействует с API Server
Получает PodSpec
Отправляет данные по состоянию
