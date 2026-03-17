---
id: CNI
aliases:
  - CNI
  - Container Network Interface (CNI)
tags: []
---

# Container Network Interface (CNI)
---
Стандарт и набор плагинов для подключения контейнеров к сети.
CNI обеспечивает возможность общения между подами и внешнем миром через сеть.

Выдача IP-адресов Pod'ам
Маршрутизация трафика между Pod'ами и нодами
Интеграция с внешними сетями


Flannel - Простой overlay network
Calico - Overlay + NetworkPolici, BGP поддержка
Cilium - Работает через eBPF, быстрый и безопасный
Weave Net - Overlay с автоматической маршрутизацией

## Принцип работы
---
Kubelet создает network namespace для pod
kubelet вызывает CNI плагин, чтобы
- Создать veth-пары
- Создать IP-адрес Pod'у
- Настроить маршруты и правила iptables/ebpf

Pod может общатся с другими Pod'ами по сети

CNI - создает интерфейс `cni0`
- Он работает как обычный L2-switch
- Соединяет все veth-интерфейсы Pod'ов на одной ноде
- Маршрутизирует по MAC-адреса

   Node (Linux)
┌───────────────┐
│     cni0      │  ← bridge (switch)
└─────┬───┬─────┘
      │   │
  vethA  vethB
    │       │
  Pod A   Pod B

### Cilium
---
**eBPF** решение
Реализует **Service** и балансировку напрямую в **Kernel** , без **iptables**


## Глоссарий
---

**Overlay Network** - Виртуальная сеть, построенная поверх физической
Технологии:
- VXLAN
- BGP
- IP-in-IP

**veth-пара** (virtual ethernet) - Пара виртуальныъ сетевых интерфейсов соединенных друг с другом.
- Создается network namespace контейнера
- Создается veth-пара
- Один конец кладется в Pod
- Второй остается на ноде

PodA - eth0 - veth pair - cni (brifge) - Node network

## Проверка
---
```bash
# Посмотреть на ноде veth
ip link
```
