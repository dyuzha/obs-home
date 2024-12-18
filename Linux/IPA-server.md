# Настройка КД FreeIPA на Astra Linux
---
## Создание контроллера домена FreeIPA
---
1. настроить бызовые параметры или воспользоваться скриптом `net_config.sh`
```bash
# IP
nmcli device modify eth0 ipv4.address 192.168.0.183

# Gateway
nmcli device modify eth0 ipv4.gateway 192.168.0.1

# DNS
nmcli device modify eth0 ipv4.dns 192.168.0.183 77.88.8.8

# Перезагрузка
sudo systemctl restart networking
```

2. Настроить имя и совершить проверку
```bash
# выдать имя хосту
hostnamectl set-hostname ipa-server

# Проверка 
nmcli device show eth0
cat /etc/resolv.conf
```
### Установка и настройка FreeIPA-server
---
```bash
# Установить необходимые пакеты

# sudo apt install fly-admin-freeipa-server   # GUI
#   Потом зайти в пуск -> сеть -> Настройка FreeIPA...

sudo apt install astra-freeipa-server         # CLI

sudo astra-freeipa-server -o -n ipa-server -d domain.local
  # -o Для изолированной среды (в тестовых целях)
# Вводим пароль (2 раза)

# Проверка запущенных служб и роллей
sudo ipactl status
```

### Удаление и переустановка FreeIPA-server
---
```bash
sudo astra-freeipa-server -U
```
