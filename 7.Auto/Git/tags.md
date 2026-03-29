---
id: tags
aliases:
  - Тегирование в git
tags: []
---

# Тегирование в git
---

```bash
# Поставить тег
git tag -a v1.0.0 -m "Первый стабильный релиз"

# Push тега
git push origin v1.0.0 # Пуш конкретного тега
git push origin -tags # Пуш всех локальных тегов сразу

# Удаление тега
git tag -d v1.0.0 # delete local
git push origin --delete v1.0.0 # delete в remote repo:
```

```bash
# Чтобы не писать команду пуша с tags
git config --global push.followTags true
```
