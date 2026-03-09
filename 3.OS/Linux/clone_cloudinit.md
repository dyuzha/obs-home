---
id: clone_cloudinit
aliases:
  - Клонирование cloudinit образа
tags: []
---

# Клонирование cloudinit образа
---
Для клонирования *cloudinit* образа (или создания шаблона)
Необходимо очеистить *machine-id*, иначе *dhcp* будет выдывать один и тотже IP

```bash
sudo cloud-init clean --logs --machine-id
```
