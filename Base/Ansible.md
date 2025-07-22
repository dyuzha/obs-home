---
id: Ansible
aliases:
  - Ansible
tags: []
---
**Back**
    [[!Base]]

# Ansible
---
Это открытый инструменнт для автоматизации IT-задач

- Управление конфигурациями
- Развертывание приложений
- Оркерстрация сервисов
- Удаленное выполненение команд

## Особенности
---
1. Агент-фри (Agentless) - не требует установки дополнительного ПО на управляемые узлы, использует SSH (Linux) и WinRM (Windows).

2. Идемпотентность - можно многократно применять одну и ту же конфигурациюк без побочных эфектов.

3. Декларативный подход

4. Модульность - сотни встроенных модулей для работы с облаками, Docker, сетями и т.д.

5. Инвентарь - список управляемых хостов с группировкой по ролям.


## Ключевые компоненты
---
- Playbooks (YAML-файлы с интсрукциями)
- Roles (переиспользуемые наборы задач)
- Inventory (файл или скрипт со списком серверов)
- Modules (готовые команды для выполнения задач)
- Templates (Jinja2 для динамических конфигов)


## Пример простого playbooks
---
```yml
- name: Installing Nginx
  hosts: web_servers
  tasks:

    - name: Install Nginx
      apt:
        name: nginx
        state: present

    - name: Start Nginx
      service:
        name: nginx
        state: started
```

## Используется
---
- DevOps для CI/CD
- Администрирование серверов
- Облачная автоматизация (AWS, Azure, GCP)
- Настройка сетевых устройств (через Ansible Network Modules)


 ## Первые шаги
---
1. Установка
```bash
# Должен был установлен python
brew install ansible
```

2.  Настройка доступа к серверам

**Парольный доступ**
Добавьте серверы в файл инвентаря (`/etc/ansible/hosts`)

```ini
[web] # Группа серверов
server1 ansible_host=192.168.1.10 ansible_use=root ansible_password=your_password
server2 ansible_host=192.168.1.11 ansible_use=ubuntu ansible_password=another_password
```

**По SSH-ключу**
 ```bash
# Сгенерируйте SSH-ключ на управляющей машине (если нет)
ssh-keygen -t ed25519

# Скопировать ключ на сервер
ssh-copy-id user@server_ip
 ```

 Создание инвентаря `inventory.ini`
 ```ini
[web]
server1 ansible_host=192.168.1.10 ansible_user=ubuntu
server2 ansible_host=192.168.1.11 ansible_user=root
 ```

 ```bash
# Показть список хостов
ansible-inventory -i /path/to/inventory.ini --list

{
    "_meta": {
        "hostvars": {
            "finland-0": {
                "ansible_host": "mrz.dyuzha.ru",
                "ansible_user": "root"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "nodes"
        ]
    },
    "nodes": {
        "hosts": [
            "finland-0"
        ]
    }
}

 # Или
ansible all -i ~/inventory.ini --list-hosts

  hosts (1):
    finland-0

 ```
