---
id: scheduler
aliases:
  - Scheduler
tags: []
---

# Scheduler
---
- Только назначает Pod на конкретные ноды
- Не запускает Pod сам
- Решение принимается на основе требований Pod и ресурсов нод

## Принцип работы
---
Pod создается (Pod не имеет assigned node (Status: Pending))
API Server пишет его в etcd
Scheduler получает Pod через watch
Sheduler проверяет требования и ресурсы нод
Scheduler выбирает подходящую ноду
Scheduler обновляет PodSpec (записывает nodeName)

Kubelet на выбранной ноде видит nodeName и запускает Pod

## Принцип выбора
---
Ресурсы: CPU, память
Node tainta/tolerarions
Node labels и Pod selectors
Affinity/Antiffinity (размезть Pod рядом/раздельно)
Pod priority / preemption
Custom policies (через scheduler extender)

```yml
# scheduler выбирет ноду с label disktype=ssd
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
  nodeSelector:
    disktype: ssd
```

## Проверка
---
```bash
kubectl get pods -A -o wide
kubectl describe pod <pod-name>
```
Node: куда назначил Scheduler
Events: как kublete начал запуск Pod

