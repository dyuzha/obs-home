---
id: hints
aliases:
  - Хинты
tags: []
---
**Back**
    [[!JS]]

# Хинты
---
Это строковые значения, которые JS передает в методы преобразования объектов, чтобы указать, в какой тип нужно преобразовать объект.
```js
let user = {
  name: "John",
  money: 1000,

  [Symbol.toPrimitive](hint) {
    alert(`hint: ${hint}`);
    return hint === "string" ? `name: ${this.name}`: this.money;
  }
}

alert(user);
alert(+user);
alert(user + 50);
```
