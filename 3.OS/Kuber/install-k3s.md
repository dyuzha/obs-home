---
id: install
aliases: []
tags: []
---



## Устпновка k3s
---

При установке необходимо указывать все SAN (Subject Alternative Names)
```bash
# Пример полной установки K3s с правильными SAN
curl -fL https://get.k3s.io | INSTALL_K3S_EXEC="--tls-san <domain> --tls-san <IP> --bind-address 0.0.0.0" sh -

# -s silent
# -f fail
# -L Следовать redirect

# -tls-san Список host'ов, для которых валиден TLS сертификат
# --bind-address слушать все сетевые интерфейсы

# будет ошибка при копировании конфига, придетсся изменять
# --bind-address 127.0.0.1


curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--tls-san k3s.dyuzha.ru --tls-san  192.168.88.14 --bind-address 0.0.0.0" sh -
```


## Проверка
---
```bash
systemctl status k3s

# Команда запуска и создает systemd unit с такими параметрами
k3s server \
  --tls-san srv-3.dyuzha.ru \
  --tls-san 141.105.66.240 \
  --bind-address 0.0.0.0

# Для изменения этих параметров, необходимо
systemctl daemon-reload
systemctl restart k3s

# Как гарантированно пересоздать сертификат

systemctl stop k3s
rm -rf /var/lib/rancher/k3s/server/tls
systemctl start k3s
```

### Запуск
---
```bash
k3s server
```
Команда запускает:
    API Server
    Scheduler
    Controller Manager
    kubelet
    containerd
    CNI (Container Network Interface)
