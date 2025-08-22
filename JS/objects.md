---
id: objects
aliases:
  - objects
  - Объекты
tags: []
---
**Back**
    [[!JS]]

# Объекты
---

## Основные действия со объектами
---

### Инициализация
---
```js
// Конструктор объекта
let user = new Object();

// Литерал объекта (Литеральная нотация)
let user = {};
```

**Литеральный синтаксис** - позволяет сразу передать несколько свойств в формате `ключ: значение`.
```js
let user = {
    name: "Dan",
    age: 19,
    "likes birds": true,
    isAdmin: true,
}
```

#### Свойство из переменной
---
Доступ к свойству через переменную доступен только с квадратными скобками!!

Создание объекта с вычисляемыми свойствами
```js
let fruit = prompt("Какой фрукт купить?", "apple");

let bag = {
    [fruit]: 5,
}

allert( bag.apple ); // 5, если fruit == "apple"
```

**Упрощенный способ создание фабричных функций**
```js
function makeUser(name, age) {
    return {
        name,   // Аналогично name: name
        age,    // Аналогично age: age
    }
}
```

### Добавление/изменение свойства
---
```js
user.sex = "man";
user["likes birds"] = false;
```

### Получение значения свойства
---
```js
allert(user.isAdmin); //true
allert(user["sex"]);  //true
```

### Удаление свойства
---
```js
delete user["likes birds"]
delete user.sex
```

### Проверка существования свойства
---
```js
allert(user.noSuchProperty === undefined); //true

// Если свойство может иметь значение undefined
allert(noSuchProperty in user); //true
```
