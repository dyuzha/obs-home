---
id: ansible-vault
aliases:
  - Ansible vault
tags: []
---

# Ansible vault
---
Зашифрованные YAML внутри Ansible

```bash
# Create
ansible-vault create vault.yml

# Vue
ansible-vault view vault.yml

# Eddit
ansible-vault edit vault.yml

# Зашифровать существующий
ansible-vault encrypt vault.yml

# Расшифровать (НЕ надо!)
ansible-vault decrypt vault.yml
```



## Способы запуска
---
```bash
ansible-playbook site.yml --ask-vault-pass

ansible-playbook site.yml --vault-password-file .vault_pass
```

## Хранение
---
| Space           | State           |
|-----------------|-----------------|
| git repo        | encrypted       |
| ansible runtime | decrypted       |
| target server   | Зависит от task |


