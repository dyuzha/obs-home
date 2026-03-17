---
id: control-manager
aliases:
  - Control Manager
tags: []
---

# Control Manager
---
Ключевая часть control plane
Дирежер кластера

- Следит за desired state кластера
- Запускает контроллеры, каждый из которых отвечает за конкретный объект Pod, Node, Deployment, Endpoint и т.д.
- обеспечивает автоматичекское исправление между фактическим состоянием и желаемым

Контроллеры внутри:
Node Controller - следит за состоянием но
Replication Controller - следит за количеством реплик Pod'ов
Endpoints Controller - связывает Service с Pod'ами
Namespace Controller - удаляет объекты, когда namespace удаляется
Service Account & Token Controller - создает default ServiceAccount и токены

Control Manager
- Запрашивает сотояние объектов
- Сравнивает с desired state
- Корректирует несовпадения через API Server


