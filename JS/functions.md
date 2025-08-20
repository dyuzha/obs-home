---
id: functions
aliases:
  - functions
tags: []
---
**Back**
    [[!JS]]

# functions
---
```js
function name(params) {
    // ... body ...
}

```

Можно использовать и изменять внешние переменные
```js
let userName = 'Vasya';

function showMessage() {
    userName = 'Petya';
    let message = `Hi, ${userName}`;
    alert(message)
}

alert(userName); // Vasya

showMessage(); // Hi, Petya

alert(userName); // Petya
```

Переменную можно "затереть" в рамках локальной видимости.
```js
let userName = 'Vasya';

function showMessage() {
    let userName = 'Petya';
    let message = `Hi, ${userName}`;
    alert(message)
}

alert(userName); // Vasya

showMessage(); // Hi, Petya

alert(userName); // Vasya
```

Выставление значения по умолчанию
```js

function showMessage(from, text = "No text") {
    alert(`${from}: ${text}`);
}

showMessage("Anna", "Hi");
showMessage("Anna");
```
В роли значения по умолчанию мб функция
```js
function showMessage(from, text = anotherFunction()) {
    alert(`${from}: ${text}`);
}

showMessage("Anna", "Hi");
showMessage("Anna");
```

Пустой `return` аналогичен ubdefined
```js
function doNothing() {
  return;
}
alert( doNothing() === undefined ); // true
```

