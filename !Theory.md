---
id: Theory
aliases:
  - Base
  - Теория
tags: []
---

# Теория
---


## 1. Аппаратное обеспечение и инфраструктура
---
[[digital-inf]] - Компьютерное представление информации
[[RAID]]
[[Processor]]
[[entropy]] - Мера случайности, которую питает генератор случайных чисел.

- серверы;
- стоечные решения;
- ЦОДы;
- сетевые устройства;
- чипы;
- периферия;
- энергоснабжение;
- охлаждение.



## 2. Сети и коммуникации
---
[[osi]] Сетевая модель OSI
[[mtcna]]
[[ftp]]
[[http]]
[[socks5]]
[[mikrotik]]
- каналы,
- маршрутизация,
- коммутация,
- WAN/LAN,
- LB,
- Firewall

### VPN
---
[[marzban]]
[[xray]]
[[shadowsocks]]
[[vless]]
[[reality]]



## 3. Операционные системы, виртуализация и контейнеризация
---
[[vps_vds]] - Отличия
[[docker_vs_lxc_lxd]] - Отличие Docker от lxc/lxd
[[ssh]]
- runtimes,
- kernel internals.

### Windows
---
[[AD]]
[[Windows]]

### Linux
---
[[!Lin]]
[[CLI]]
[[IPA-client]]
[[IPA-server]]
[[Memory]]
[[More-apps]]
[[Notice]]
[[SELinux]]
[[Packet-mn]]
[[Special_permission_bits]]
[[Units]]
[[admin]] - Админские команды (база)
[[alternatives]]
[[archive]]
[[awk]]
[[cgroups]]
[[chroot]]
[[curl]]
[[devices]]
[[fail2ban]]
[[file]]
[[firewalld]]
[[fstab_conf]]
[[gpg_conf]]
[[kerberos]]
[[mount_autmount-unit]]
[[ngrok]]
[[novigation]]
[[oom-killer]]
[[pacman]]
[[ranger]]
[[process]]
[[scp]]
[[sed]]
[[socat]]
[[ssh-copy-id]]
[[ssh]]
[[sshfs]]
[[sysctl]]
[[systemd]]
[[term]]
[[tmux]]
[[wget]]
[[wget_vs_curl]]



### Контейнерные менеджеры
- snap
-

### Гипервизоры (KVM, VMware)
---
[[!PM]] - ProxMox
[[proxmox]]
[[virtio]]
[[vm-cloud-init]]
[[vm-set-graphic]]
[[vm-set-disks]]
[[vm-set-net]]
[[vm-set-rng]]

[[vps_vds]] (Пустой но с ссылкой)
Базовая информация про виртуальное решение управления ИТ-инфраструктурой


### Контейнеризация
---
[[!Docker]]
    [[Compose]]
    [[architecture]] - Архитектура Docker'а
    [[cmd]] - Команды
    [[dockerfile]]
    [[dockerhub]]
    [[drivers]]
    [[linux-lab]]
    [[namespace-container]]
    [[volumes]]

- LXC

### Орекстрация
---
- docker-compose (podman-compose)

[[Kuber]]
    - [[k8s]]
    - k3s
    - minikube
    - docker swarm



## 4. Облачные и платформенные сервисы
---
- IaaS/PaaS/FaaS/SaaS у крупных провайдеров (AWS/GCP/Azure и др.),
- region/zone,
- облачные сервисы (compute, storage, managed DB).



## 5. Хранение данных и базы данных
---
[[DB]]
[[SQLite]]
[[db-cons]]
[[maria-db]]
PostgreSQL

- блочное/объектное/файловое хранилище,
- реляционные и нереляционные БД,
- репликация,
- бэкапы,
- консистентность.


## 6. Разработка ПО и архитектура приложений
---
[[Web-servers]] (Apache/Nginx)
    - Apache,
    - Nginx,
    - Caddy,
    - Traefik;

[[arch-proxy]] (Базовая информация про прокси и его виды)
- Обратный прокси
- Прозрачный прокси
- Балансировщик нагрузки

Gateways:
    [[asgi]]
    [[wsgi]]


[[api]] (API-дизайн)
[[arch-api]]
- Цели использования
- Виды API
- Преимущества и недостатки
- Различия между протоколами API
    - RESTfil API
    - SOAP
    - GraphQL
    - JSON-RPC и XML-RPC

[[Radicale]]
[[CalDav]]
[[htpasswd]]
[[LDAP]]
[[acmes.sh]]
[[nginx]]

### Языки
---
[[!Pyhton]]

[[!Bash]]
    [[cases]]
    [[exec]]
    [[find]]
    [[grep]]
    [[pipe]]
    [[syntax]]

[[JS]]
    [[!JS]]
    [[Date]]
    [[arrays]]
    [[base_operators]]
    [[bits_operators]]
    [[cicles]]
    [[clean_code]]
    [[conditional]]
    [[copy_objects]]
    [[data_types]]
    [[functions]]
    [[global_reestr_symbol]]
    [[global_var]]
    [[hints]]
    [[iterables]]
    [[logical_operators]]
    [[map]]
    [[method]]
    [[moduls]]
    [[more]]
    [[numbers]]
    [[objects]]
    [[operator-new]]
    [[optional_chain]]
    [[set]]
    [[spavn_operators]]
    [[string]]
    [[symbol]]
    [[test]]
    [[use_strict]]
    [[web_worker]]

[[Lua]]
    [[Reference]]
    [[featch]]

[[PowerShell]]

- фреймворки,
- микросервисы,
- монолиты,
- тестирование
- паттерны проектирования.


## 7. Автоматизация, CI/CD & IaC
---
[[!Git]]
    [[Base]]
    [[Cases]]
    [[Conflicts]]
    [[GitHubCli]]
    [[LazyGit]]
    [[Merge]]
    [[Reference]]
    [[Stage]]
    [[Stash]]
    [[sparse-checkout]]
    [[ssh]]

инструменты и практики для автоматизации:
- сборок,
- тестов,
- деплоймента,
- конфигурации (Jenkins/GitHub Actions/Ansible/Terraform/etc.).

[[IaC]]
Инфраструктура как код

[[ansible]]
[[Ansible]]
    [[playbooks_vs_roles]]
    Раздница между playbooks и roles

[[ci_cd]]
[[workflow]]
    [GitHub Actions](gh-actions)
    [Gitlab CI/CD](gitlab-ci-cd)
    [[Jetkins]]

## 8. Наблюдаемость, логирование и управление инцидентами
---
— метрики,
- трассировка,
- лог-агрегация,
- APM,
- алёртинг,
- playbooks,
- RCA.

## 9. Безопасность и управление доступом
---
- сетевые границы,
- IAM,
- PKI,
- безопасность SDLC,
- мониторинг угроз.

### Уязвимости
---
[[kiber]] - Виды kiber-атак

### Шифрование
[[entropy]] Энтропия - основа для генерации случайности
    [[GPG]]

[[kiber-certs]]
- Что такое TLS/SSL
- Виды TLS сертификатов
- Сертификаты для кириллических доменов

[[kiber-ACME]] - протокол для выпуска сертификатов


## 10. Управление и эксплуатация (Operations, SRE)
---
процессы (инцидент-менеджмент, change management),
SLIs/SLOs/SLAs,
runbooks,
автоматизация рутинных задач.

## 11. Управление, соответствие и финансы
---
- политики,
- регуляции (GDPR, HIPAA и т.д.),
- аудит,
- учёт затрат в облаке (FinOps).



## Прочее
---
[[regular]]
Регулярные выражения (*теория и реализация*)
[[BEM]]
Методолгия программ и интерфейсов
