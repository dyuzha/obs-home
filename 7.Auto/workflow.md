---
id: workflow
aliases:
  - workflow
tags: []
---
**Back**
    [[!!Base]]

# workflow
---

[GitHub Actions](gh-actions)
[Gitlab CI/CD](gitlab-ci-cd)
[[Jetkins]]

*Рабочий процесс* - автоматизированная последовательность шагов, которая выполняется при определенных условиях (например, при `git push` или по расписанию)
 *В контексте CI/CD DevOps:*

Workflow определяет, как код
- тестируется
- собирается
- развертывается

Запускается на событие
- push
- PR
- cron-task
- ...

Состоит из jobs/steps отдельные задачи, например:
- линтинг
- тесты
- деплой


## Структура
---
| Компонент   | Описание                                  |
|-------------|-------------------------------------------|
| Trigger     | Событие запускающее workflow              |
| Jobs        | Отдельные задачи                          |
| Steps       | Команды внутри                            |
| Artifacts   | Файлы, сохраняемые после job              |
| Environment | Переменные окружения (секреты, версии ПО) |


1. Trigger
Событие запукающее workflow
- push
- pull_request
- schedule

2. Jobs
Отдельные задачи
- test
- build
- deploy

3. Steps
Команды внутри job
- run
- docker build
- pytest

4. Artifacts
Файлы, сохраняемые после job
- `*.log`
- `*.bin`

5. Environment
Переменные окружения
- секреты
- версии
- ПО
