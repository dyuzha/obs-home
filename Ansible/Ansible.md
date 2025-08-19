---
id: Ansible
aliases: []
tags: []
---

```yml
- name: Собрать информацию о службах
  ansible.builtin.service_facts:

- name: Показать все данные о службах
  ansible.builtin.debug:
    var: ansible_facts.services
```

Примерный вывод
```json
"services": {
    "apache2": {
        "name": "apache2",
        "source": "systemd",
        "state": "running",  # работает
        "status": "enabled", # включена в автозагрузку
        "pid": 1234
    },
    "ssh": {
        "name": "ssh",
        "source": "sysvinit",
        "state": "running",
        "status": "enabled",
        "pid": 5678
    }
}

```
Практическое применение

```yml
- name: Перезапустить Apache, если он работает
  ansible.builtin.service: # управление сервисами
    name: apache2
    state: restarted
  when: ansible_facts.services.apache2.state == "running"

- name: Завершить выполнение, если служба не работает
  ansible.builtin.fail: # Остановка задачи
    msg: "Nginx не запущен!"
  when: ansible_facts.services.nginx.state != "running

- name: Показать работающие службы
  ansible.builtin.debug:
    msg: "Запущенные службы: {{ ansible_facts.services | dict2items | selectattr('value.state', 'equalto', 'running') | map(attribute='key') | list }}"
```
