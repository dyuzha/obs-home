---
id: gitlub-runner
aliases:
  - gitlub-runner
tags: []
---

# gitlub-runner
---
1. Установка репозитория
```bash
# Deb
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" | sudo bash

# Rhell
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.rpm.sh" | sudo bash
```

2. Установка runner'а
```bash
# Deb
apt install gitlab-runner

# Rhell
dnf install gitlab-runner
```

3. Разрешаем автозапуск и стартуем
```bash
systemctl enable gitlab-runner --now
```

4. Регистрация в проекте
```bash
gitlab-runner register  --url https://gitlab.com  --token <token>
```

5. Проверка
```bash
gitlab-runner run
systemctl enable gitlab-runner
```

6.
```bash
# Генерируем ключ
ssh-keygen -t ed25519 -C "gitlab-ci-deploy" -f ~/.ssh/id_ed25519

# Копируем на сервер
ssh-copy-id -i ~/.ssh/id_ed25519.pub deployer@server.com
```
