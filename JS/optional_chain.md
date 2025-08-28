---
id: optional_chain
aliases:
  - optional_chain
tags: []
---
**Back**
    [[!JS]]

# optional_chain
---
`?.` - специальная синтаксическая конструкция

```js
let user = {}; // пользователь без адреса

alert( user?.address?.street ); // undefined (без ошибки)
```
Считывание адреса с помощью user?.address работает, даже если объект user не существует:
```js
let user = null;

alert( user?.address ); // undefined
alert( user?.address.street ); // undefined
```
```js
let key = "firstName";

let user1 = {
  firstName: "John"
};

let user2 = null;

alert( user1?.[key] ); // John
alert( user2?.[key] ); // undefined
```

Использование для вызова функций
```js
let userAdmin = {
  admin() {
    alert("Я админ");
  }
};

let userGuest = {};

userAdmin.admin?.(); // Я админ

userGuest.admin?.(); // ничего не произойдет (такого метода нет
```
Удаление
```js
delete user?.name; // удаляет user.name если пользователь существует
```

**Нельзя использовать для записи!!!**
```js
let user = null;

user?.name = "John"; // Ошибка, не работает
// то же самое что написать undefined = "John"
```
