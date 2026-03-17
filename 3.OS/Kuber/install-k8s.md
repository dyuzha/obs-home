---
id: install
aliases: []
tags: []
---



## Открыть kuber во внешку при установки
---

При установке необходимо указывать все SAN (Subject Alternative Names)
```bash
# Пример полной установки K3s с правильными SAN
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--tls-san srv-3.dyuzha.ru --tls-san 141.105.66.240 --bind-address 0.0.0.0" sh -
```


## Открыть kuber во внешку после установки и запуска
---

Официальная документация K3s предписывает открыть следующие порты и диапазоны:
```bash
# Порт 6443/TCP для API-сервера:
firewall-cmd --permanent --add-port=6443/tcp # лучше сделать, как в пункте ниже

# Подсеть 10.42.0.0/16 для трафика между подами:
firewall-cmd --permanent --zone=trusted --add-source=10.42.0.0/16

# Подсеть 10.43.0.0/16 для внутренних сервисов:
firewall-cmd --permanent --zone=trusted --add-source=10.43.0.0/16
```

### Открыть порт для k8s
---
```bash
# 1. Сначала узнайте ваш текущий публичный IP
# На вашей локальной машине (PROF-07) выполните:
curl ifconfig.me
# Или
curl icanhazip.com

# 2. На сервере srv-3 создайте зону для вашего IP
sudo firewall-cmd --permanent --new-zone=k8s-access

# 3. Добавьте ваш IP в зону
sudo firewall-cmd --permanent --zone=k8s-access --add-source=ВАШ_IP/32

# 4. Откройте порт 6443 только в этой зоне
sudo firewall-cmd --permanent --zone=k8s-access --add-port=6443/tcp

# 5. Убедитесь, что в публичной зоне порт 6443 ЗАКРЫТ
sudo firewall-cmd --permanent --remove-port=6443/tcp --zone=public 2>/dev/null || true

# 6. Примените изменения
sudo firewall-cmd --reload

# 7. Проверьте настройки
sudo firewall-cmd --zone=k8s-access --list-all
```


Проверка
```bash
nc -zv domain.ru 6443
```


### Перегенерировать сертификаты
---

Останавливаем службу
```bash
systemctl stop k3s
```

Редактируем /etc/rancher/k3s/config.yaml
```yaml
tls-san:
  - "domain.ru"
  - "IP"
  - "domain (имя сервера)"
  - "localhost"
  - "kubernetes"
  - "kubernetes.default"
  - "kubernetes.default.svc"
  - "kubernetes.default.svc.cluster.local"
bind-address: "0.0.0.0"
advertise-address: "IP"
```
Перегенирирование
```bash
# Удалите старые сертификаты
sudo rm -rf /var/lib/rancher/k3s/server/tls

# Перезапустите K3s
sudo systemctl start k3s
```

## Проверка
---
```bash
# Посмотреть события в кластере
kubectl get events --sort-by='.lastTimestamp'

# Проверка установки системный компонентов
kubectl get pods -n kube-system
kubectl get pods -n kube-system -w  # следить за изменениями

NAME                                      READY   STATUS      RESTARTS   AGE

# Днс сервер для кластера
coredns-7f496c8d7d-6fjs9                  1/1     Running     0          17h

# Установшик CRD для Traefik (Выполнил, завершился)
helm-install-traefik-crd-kv7vc            0/1     Completed   0          17h

# Установшик Traefik (Выполнил, завершился)
helm-install-traefik-gtmbn                0/1     Completed   1          17h

# Динамическое выделение storage
local-path-provisioner-578895bd58-mfml9   1/1     Running     0          17h

# Сбор метрик (если 0/1 - перезапустить)
metrics-server-7b9c9c4b9c-mdbc9           0/1     Running     0          17h

# LoadBalancer для Traefik
svclb-traefik-82943bd1-c6jdj              2/2     Running     0          17h

# Ingress контроллер
traefik-6f5f87584-lnjc7                   1/1     Running     0          17h

# Посмотреть использование ресурсов
kubectl top nodes
kubectl top pods -A
```
Перезапустить метрик
```bash
kubectl delete pod metrics-server-7b9c9c4b9c-mdbc9 -n kube-system
```

Проверка всех ключевых
```bash
kubectl get pods -n kube-system -l 'app in (coredns, traefik, local-path-provisioner)')'
NAME                                      READY   STATUS    RESTARTS   AGE
local-path-provisioner-578895bd58-mfml9   1/1     Running   0          17h
```

## Тест работоспособности
```bash
# 1. Создадим тестовый под
kubectl run test --image=nginx --restart=Never

# 2. Проверим, что под запустился
kubectl get pods test

# 3. Проверим логи (должны быть логи nginx)
kubectl logs test

# 4. Удалим тестовый под
kubectl delete pod test
```


