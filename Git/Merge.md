---
id: Merge
aliases:
  - Merge
tags: []
---
**Back**
    [[!Git]]

# Merge
---
Объединяет изменения из одной ветки в другую
- `Feature/A1` -> `main`
Включение изменений из одной ветки в другую
- `Feature/A1` -> `main` <- `Feature/A2`
Решение задач параллельной разработки (Несколько людей параллельно трудятся над одним проектом)
- `Feature/A1` <- `main`
Обновление текущей ветки актуальными изменениями в другой

```bash
# current-branch <- source-branch
git merge <source-branch>
```

## Типы слияния
---

### Fast Forward merge
---
Быстрая перемотка
*Работает только если текущая ветка не имеет новых коммитов после ответвления*
```bash
git merge --ff-only feature
```


### Recursive merge
---
Рекурсивное слияние
*Если в обоих ветках есть новые комииты*
Git создает слияние -> commit слияния имеет 2ух родителей
```bash
git merge feature  # автоматически выбирает стратегию
```


### Squash merge
---
Слияние с уплотнением
*Если нужно объединить все коммиты из `Feature` в один новый комиит `main` БЕЗ СОХРАНЕНИЯ ИСТОРИИ*
```bash
git merge --squash feature
git commit -m "Требует явный коммит"
```


### Ours/Theirs merge
---
Принудительное разрешение конфликтов
```bash
git merge -Xours feature  # игнорирует конфликты в пользу текущей ветки
git merge -Xtheirs feature  # игнорирует конфликты в пользу Feature ветки
```


## Отмена слияния
---
Если слияние еще не закомиченно
```bash
git merge --abort
```

Если коммит уже создан
```bash
# Откат на 1 коммит назад
git reset --hard HEAD~1 # С потерей изменений
git reset --soft HEAD~1 # Изменения помещаются в индекс

# Создание отменяющего коммита
git revert -m 1 <merge-commit-hash>
```




