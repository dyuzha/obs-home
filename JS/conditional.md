---
id: conditional
aliases:
  - conditional
  - Условные ветвления
tags: []
---
**Back**
    [[!JS]]

# Условные ветвления
---
```js
let name = prompt("input you name", "NoName");

if (name === "admin") {
    alert('Hi super user!')
} else if (name === "NoName"){
    alert('Hi anonym')
} else {
    alert(`Hi ${name}`)
}
```

## Тернарный оператор "?"
---
```js
let result = conditional ? value1 : value2
```

```js
let age = prompt("Сколько вам лет?", "");

let accessAllowed = age > 18 ? true : false;

// По идеи можно так
// let accessAllowed = age > 18
alert(accessAllowed);
```
```js
let name = prompt("input you name", "NoName");

let message = (name === "admin") ? "Hi super user!" :
    (name === "NoName") ? "Hi anonym" :
    `Hi ${name}`

alert(message);
```
