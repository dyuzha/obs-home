---
id: IPA-client
aliases: []
tags: []
---
**Back**
    [[!Lin]]

**More**
    [[IPA-server|ipa-server]]
    [[LDAP]]


# IPA-client
---

## Ввод клиентской машины Astra Linux в домен FreeIPA
---

#### Необходимые условия для создания контроллера домена FreeIPA:
---
Клиент и сервер должны находиться в одной широковещательной сети и иметь доступ друг к другу
```bash
# Проверка
ping client
```
Не должно быть пакетов для работы со сторонними доменами

#### Произвести настройки сетевого интерфейса
---
...


### Добавление машины в домен FreeIPA
---

#### 1. Активация сетевого интерфейса
---
```bash
ping <IP-controller_domains>

sudo hostnamectl set-hostame <ws_name>
sudo hostnamectl set-hostame astraclassic

# Файл /etc/hosts
127.0.0.1 localhost
127.0.1.1 <hostname>

# Получить список сетевых подключений
nmcli con show

# Назначить сетевому подключению сетевую карту
sudo nmcli con mod "Проводное соединение 1" connection.interface-name eth0

```

#### 2. Настройка DNS
---

##### 2.1. Настройка DNS через Network Manager
---
Выбрать один из способов настройки DNS
```bash

# Запретить использование ip-адресв сервера DNS, предоставляемы DHCP-сервером
sudo nmcli con mod "Проводное соединение 1" ipv4.ignore-auto-dns yes

# Указать IP-адрес (IP-адреса) КД, и, опционально, отделенный пробелом IP-адрес внешнего сервера DNS (требуется если клиенту необходим доступ в Интернет, а перенаправление запросов DNS не включено на КД). Для примера в качестве внешнего DNS указан DNS Яндекс (IP-адрес 77.88.8.8):
sudo nmcli con mod "Проводное соединение 1" ipv4.dns "<IP-адрес КД> 77.88.8.8"
sudo nmcli con mod "Проводное соединение 1" ipv4.dns "192.168.0.183 77.88.8.8"

# Перезапустить (выключить и включить) сетевое подключение. Это лучше всегда делать одной командой, чтобы не потерять связь с настраиваемым компьютером при работе через удаленное подключение (например, через SSH или при настройке с помощью сценариев Puppet/Ansible):
sudo nmcli con down "Проводное соединение 1" ; sudo nmcli con up "Проводное соединение 1"
```

##### 2.2. Настройка DNS через Networking.service
---
```bash
# Отредактировать /etc/resolv.conf
search domain.local
nameserver 192.168.0.183        # IP-адрес КД
nameserver 77.88.8.8            # DNS - Яндекса

# Перезапустить сервис
sudo systemctl restart networking
```

#### 3. Установка пакетов
---
```bash
# Устанавливаем один из пакетов
 sudo apt install astra-freeipa-client     # CLI
```

#### 4. Ввод машины в домен
---

##### 4.1 GUI
---
- Открыть GUI-клиент
  a) **ПУСК** -> **Парметры** -> **Клиент и сервер** -> **Настройка FreeIPA клиент Fly**
  b) **ПУСК** -> **Панель управления** -> **Сеть** -> **Настройка FreeIPA клиент Fly**

- Ввести
  Домен: ipa-server.domain.local
  Логин: admin *(логин администратора домена)*
  Пароль: ****** *(Пароль администратора домена)*

- Нажать кнопку **Подключиться**

##### 4.2 CLI
---



## Вывод клиентской машины Astra Linux из домена FreeIPA
---

### 1. На КД
``````bash

