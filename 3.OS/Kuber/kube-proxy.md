---
id: kube-proxy
aliases:
  - kube-proxy
tags: []
---

# kube-proxy
---
Реализует абстракцию **Service** на уровне сети
- Без него нельзя использовать ClusterIP
- DNS
- Отсутствие балансировки между подами

API Server
|
kube-proxy (на каждой ноде)
- Читает Service и Endpoints
- Настраивает iptables / IPVS
|
Сеть ноды (через OS)

