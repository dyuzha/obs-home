---
id: symbol
aliases:
  - symbol
tags: []
---
**Back**
    [[!JS]]

# symbol
---
Символ - уникальный идентификатор

```js
let id = Symbol();

// Создание символа с именем (описанием) - id
let id = Symbol("id");
```

Символы - уникальны.
Одинаковое описание - разные символы.

```js
let id1 = Symbol("id");
let id2 = Symbol("id");

alert(id1 == id2); // false
```

Символы - Не преобразуются автоматически в строки
```js
let id = Symbol("id");
alert(id); // TypeError: Cannot convert a Symbol value to a string

alert(id.toString()); // Symbol(id)
alert(id.description); // id
```

## Скрытые свойства объектов
---
```js
let user = {
  name: "Вася"
};

let id = Symbol("id");

user[id] = 1;

alert( user[id] ); // мы можем получить доступ к данным по ключу-символу
```

## Символы в литеральной записи объектов
---

```js
let id = Symbol("id");

let user = {
  name: "John",
  [id]: 123,
}
```

## Поведение при итерации
---
Свойства, чьи ключи - символы, не перебираются циклом `for ... in`
```js
let id = Symbol("id");

let user = {
  name: "John",
  age: 23,
  [id]: 123,
}

for (let key in user) alert(key); // name, age
```
Если другой скрипт, другая библиотека, будут работать с данным объектом, то при переборе, они не получат символьное свойство.

`Object.assign` - копирует и строковые и символьные свойства.
