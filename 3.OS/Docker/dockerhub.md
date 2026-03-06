---
id: dockerhub
aliases:
  - dockerhub
tags: []
---

# dockerhub
---

## Публикация image на dockerhub
---

1. Регистрация на dockerhub

2. Аунтефикация в консоли
```bash
docker login
```

3. Сборка образа
```bash
docker build -t myapp:latest .
```

4. Тегирование образа
```bash
docker tag local_image_name username/repo_name:tag

# Например
docker tag myapp:latest myusername/myapp:latest
```

5. Публикация (push)
```bash
docker push myusername/myapp:latest
```

