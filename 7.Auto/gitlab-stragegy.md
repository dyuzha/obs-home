---
id: gitlab-stragegy
aliases:
  - Gitlab-ci стратегия
tags: []
---

# Gitlab-ci стратегия
---
1. Gitlab (project settings)
- Создать runner

2. Ansible (gitlab_runner)
- Развертывание runner
- Регистрация runner

3. Ansible (project)
- Развертывание проекта на сервере
- Настройка ssh проекта для giltab-runner

4. Настройка pipelines (Gitlab-ci)
- `stage`
    - теги:
       - commit hash
       - git tag

- `main`
    - теги:
      - commit hash
      - git tag

5. Gitlab (registry)
- Включение автоочистки по правилам:
    - Оставлять теги, совпадающие с Git-тегами
    - Удалять теги старше 30 дней, если это не latest


## Логика pipeline
---
Ветка stage:
- push -> deploy на stage сервер с hash коммита
- push с тегом -> deploy на stage сервер
    - с hash коммита
    - c git тегом

Ветка main:
- push - Все тоже самое, что и у stage, но + происходит push с тегом latest


## Использование
---
1. Разработка:
- Используем ветку dev

2. Пред продакшен:
- (merge dev in stage,) push в ветку stage

3. Продакшен:
```bash
# Тегирование в ветке stage
git tag -a v1.0.0 -m "Первый стабильный релиз"

# push тега в ветке stage -> Вызовет deploy_prod
git push origin v1.0.0 # Пуш конкретного тега

# merge в ветку main -> Вызовет тегирование образа - latest
# !!! Важно: Для чистоты, merge должен выполняться только
# с ПОСЛЕДНИМ ТЕГИРОВАННЫМ коммитом
git checkout main
git merge stage
git push origin main
```

### Нейминг (SemVer)
---
Теги именуются по системе Semantic Versioning:
v1.0.0 — мажорная версия (большие изменения, ломающие совместимость).
v1.1.0 — минорная версия (новый функционал).
v1.1.1 — патч (исправление багов).
