---
id: global_reestr_symbol
aliases:
  - global_reestr_symbol
tags: []
---
**Back**
    [[!JS]]

# global_reestr_symbol
---
`Symbol.for(key)` - обратиться к глобальному реестру символов по ключу

```js
// Читаем символ из глобального реестра и записываем в переменную
let id = Symbol.for("id"); // Если символа не существует, он будет создан

// Читаем символ снова и записываем в переменную
let idAgain = Symbol.for("id");

allert(id === idAgain); // true
```
