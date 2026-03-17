---
id: api-server
aliases:
  - API Server
tags: []
---

# API Server
---
**HTTP REST**
**HTTPS :6443**

Центральный хаб управления Kubernetes-кластером
Сервер посредник между компонентами и Etcd

клиенты:
- Kubectl
- Scheduler
- Control Manager
- Внешние программы (client-go, api)

Принимает REST-запросы
Проверяет аутентификацию, авторизацию
Валидация объектов Kubernetes (Pod, Deployment, Service, и тд)
Общение между компонентами
Сохраняет состояние в etcd

kubectl / client-go / ...
       │
       ▼
   API Server
       │
   validate → authenticate → authorize
       │
       ▼
     etcd (сохраняем desired state)


Примеры запросов:
Scheduler: "Какие Pod нужно запланировать?"
Control Manager: "Какое текущие состояние объектов?"
Kubectl: Сообщает статус Pod и получает инструкцию для запуска/удаления
Custom Controlles / Operators: взаимодействует с кластером через API

Примеры взимодействия:
Scheduler автоматически выбирает ноды для Pod
Control Manager создает ReplicaSet, чтобы поддерживать нужное количество Pod
Operator создает CRD и управляет приложением
Kubelet отправляет heartbeat и статус Pod


## Проверка
---
```bash
kubectl get --raw=/healthz
kubectl get --raw=/version
```


