---
id: playbooks_vs_roles
aliases:
  - playbooks_vs_roles
tags: []
---
**Back**
    [[!Base]]
    [[Ansible]]

# playbooks_vs_roles
---
Разница между playbooks и roles

## Playbook
---
- Разово выполнить набор задач (например, перезапуск сервисов)
- Простые сценарии (1-2 задачи)
- Интегрировать готовые `Roles`

```yaml
- name: Deploy Web App
  hosts: webservers
  tasks:
    - name: Install Nginx
      apt:
        name: nginx
        state: present
    - name: Copy config
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
```

Playbook с Role (site.yml):
```yaml
- name: Configure Nginx
  hosts: webservers
  roles:
    - nginx  # Всё из roles/nginx/ автоматически подключается
```


## Roles
---
- Создать переиспользуемый компонент (например, установка Docker)
- Разделить логику (например, отдельные роли для Nginx, PostgreSQL, Redis)
- Упростить поддержку больших проектов

```sh
roles/nginx/
├── tasks/                  # Основные задачи
│   └── main.yml
├── templates/              # Шаблоны конфигов
│   └── nginx.conf.j2
└── defaults/               # Переменные по умолчанию
    └── main.yml
```


---
**Playbook**  — это сценарий выполнения задач.

**Role** — это модульный компонент, который можно встраивать в Playbooks.

**Best Practice** : Для сложных проектов используйте Roles + Playbooks как "точки входа"
