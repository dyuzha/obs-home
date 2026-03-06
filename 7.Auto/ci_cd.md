---
id: ci_cd
aliases:
  - ci/cd
  - CI/CD
  - CI/CD (Непрерывная интеграция и доставка)
tags: []
---
**back**
    [[!!Base]]

# CI/CD (Непрерывная интеграция и доставка)
---
-- Методология автоматизации процессов:
- CI (Continuous Integration) - автоматическое тестирование и сборка кода
- CD (Continuous Delivery/Deployment) - автоматическое развертывание

[GitHub Actions](gh-actions)
[Gitlab CI/CD](gitlab-ci-cd)
[[Jetkins]]

## Пример CI/CD:
---
1. Разработчик пушит код -> CI запускает тесты.
2. Если тесты прошли -> CD деплоит код на сервер.

 ## Пример CI/CD pipline (Gitlab CI/CD)
 ```yml
 stages:
    - test
    - deploy

test_job:
    stage: test
    script:
        - pytest

deploy_job:
    stage: deploy
    script:
    - ansible-playbook deploy.yml
```
