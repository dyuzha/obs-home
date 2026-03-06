---
id: method
aliases:
  - Методы и контекст
tags: []
---
**Back**
    [[!JS]]

# Методы и контекст
---

## Инициализация
---
```js
let user = {
  name: "John",
  age: 30
};

user.sayHi = function() {
  alert(`Hi, my name is ${this.name}`);
};
```

Определение методов в литеральной записи.
```js
let user = {
  name: "John",
  age: 30,
  sayHi() {
    alert(`Hi, my name is ${this.name}`);
  }
};
```
