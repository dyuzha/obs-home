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
gitlab-runner register  --url https://gitlab.com  --token glrt-k6jFdwVHwCSBmiE1UvZFD286MQpwOjFibzB2bwp0OjMKdTppYXBvdxg.01.1j1xf7n4j
```

5. Проверка
```bash
gitlab-runner run
```
