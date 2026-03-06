---
id: gitlab-ci-cd
aliases:
  - gitlab-ci-cd
tags: []
---
**Back**
    [[!!Base]]
    [[workflow]]
    [[ci_cd]]

# gitlab-ci-cd
---

```yaml
stages:
  - test

test:
  stage: test
  image: docker:24
  services:
    - docker:dind
  script:
    - docker build -t bash-tester -f Dockerfile .
    - docker run --rm bash-tester bats tests/
```
