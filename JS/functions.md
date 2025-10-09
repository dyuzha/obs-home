---
id: functions
aliases:
  - Functions
tags: []
---
**Back**
    [[!JS]]

# Functions
---

## Обычные функции
---
- Имеют собственный *this*
- *this* определяется в момент вызова функции
- Зависит от контекста вызова

### Основы
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

Пустой `return` аналогичен `undefined`
```js
function doNothing() {
  return;
}
alert( doNothing() === undefined ); // true
```

### Виды определения
---

#### Function declaration
---
- Функция объявляется отдельной конструкцией
- Можно вызвать до определения
- В строгом режиме, когда функция создается внутри блока `{}`, ее можно использовать только внутри блока.
```js
// Function Declaration
function sum(a, b) {
  return a + b;
}
```

#### Function expression
---
- Создается внутри другого выражения иди конструкции
- Функция создается, когда интерпритатор доходит до нее => нельзя вызывать до определения
- В строгом режиме, когда функция создается внутри блока `{}`, ее можно использовать ВНЕ БЛОКА
```js
// Function Expression
let sum = function(a, b) {
  return a + b;
};
```

## Стрелочные функции
---
- Не имеют собственного контекста (this)
- *this* заимствуется из внешней области
- *this* фиксируется в момент создания

### Виды опредения
---

#### Однострочные
---
```js
let func(arg1, arg2, ... argN) => expression;

// Аналог
function func(arg1, arg2, ..., argN) {
    expression;
}
```

Пример:
```js
let sum = (a, b) => a + b;

alert(sum(4, 5))
```
Если один аргумент - скобки можно опустить
```js
let double = n => n * 2
```
Если нет аргументов, нужны скобки
```js
let sayHi = () => alert("Hi!")
```

#### Многострочные
---
```js
let sum = (a, b) => {
    let result = a + b;
    return result;
};
```
