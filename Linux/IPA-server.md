# Настройка КД FreeIPA на Astra Linux
---
## Создание контроллера домена FreeIPA
---

### Произвести настройки сетевого интерфейса
---
```bash
# выдать имя хосту
hostnamectl set-hostname ipa-server.domain.local
```
Настроить бызовые параметры
```bash
# IP
nmcli device modify eth0 ipv4.address 192.168.0.178

# Gateway
nmcli device modify eth0 ipv4.gateway 192.168.0.1

# DNS
nmcli device modify eth0 ipv4.dns 192.168.0.178 77.88.8.8

# Перезагрузка
sudo systemctl restart networking

# Проверка 
nmcli device show eth0
cat /etc/resolv.conf
```
или воспользоваться скриптом `networ_config.sh`

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
```bash
sudo astra-freeipa-server -U
```
