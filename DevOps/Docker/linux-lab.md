---
id: linux-lab
aliases:
  - linux-lab
tags: []
---
**Back**
    [[!Docker]]

# linux-lab
---

```bash
docker run -it --rm --name linux-lab ubuntu:latest /bin/bash
-it # Интерактивный режим с терминалом
--rm # Автоматически удалит контейнер после завершения
ubuntu:latest # Образ ОС (можно любой другой)
linux-lab # Имя контейнера
/bin/bash # Команда которую нужно запустить
```

## Более тонкий вариант
---
```dockerfile
FROM ubuntu:latest

# Обновление и установка пакетов
RUN apt update && apt install -y \
    curl \
    git \
    vim \
    python3 \
    ranger \
    cron \
    && rm -rf /var/lib/apt/lists/*

# Дополнительные настройки (опционально)
WORKDIR /experiments
CMD ["/bin/bash"]
```

```bash
docker build -t my-linux-lab .
docker run -it --rm --name linux-lab my-linux-lab
```

