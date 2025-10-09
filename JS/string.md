---
id: string
aliases:
  - Строки
tags: []
---
**Back**
    [[!JS]]

# Строки
---
Внутрений формат строк ВСЕГДА UTF-16
Строки **неизменяемы**.


## Методы
---
```js
let str = `Hello`;

// Обращение по индексу
alert( str[0] ); // H
alert( str.at(0) ); // H

alert( str[str.length - 1] ); // o
alert( str.at(-1) ); // o


// Изменения регистра
str.toUpperCase()
str.toLowerCase()
```


## Свойства
---
```js
str = "Hello"

// Длина
str.length // Без круглых скобок
```

## Языковые конструкции
---
### Перебор по символьно
---
`for ... of`
```js
for (let char of 'Hello') {
    alert(char);
}
```

