---
id: operator-new
aliases:
  - operator new
  - Конструктор оператор new
  - Конструктор, оператор new
tags: []
---
**Back**
    [[!JS]]

# Конструктор, оператор new
---
Оператор `new`
Позволяет создать один объект.

## Функция-конструктор
---
1. Имя функции-конструктора, должно начинаться с большой буквы.
2. Функция-коструктор должна выполняться, только с помощью оператора `new`.

```js
function User(name) {
  // this = {}; Неявно

  this.name = name;
  this.isAdmin = false;
  this.sayHi = function() {
    alert(`My name is ${this.name}`);
  };

  // return this; Неявно
}

let user = new User("Jack");

alert(user.name); // Jack
alert(user.isAdmin); // false
```



