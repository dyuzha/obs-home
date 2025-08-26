---
id: copy_objects
aliases:
  - Копирование объектов и ссылки
  - Копирование и объединение объектов
tags: []
---

# Копирование и объединение объектов
---
Отличие объектов от примитивов:
Объекты хранятся и копируются "по ссылке", тогда как примитивные значения:
- строки;
- числа;
- логические значения;
- ..., копируются "как целое значение"

**Копирование объектной переменной создает еще одну ссылку на новый объект.**

Два объекта равны, только в том случае, если это один и тот же объект.

```js
let user = {
  name: "John",
  age: 30
};

let clone = {};

for (let key in user) {
  clone[key] = user[key];
};

clone.name = "Vasya";

alert(user.name); // "John"
```
## Вложенное (Глубокое) копирование
---
```js
let user = {
    name: "John",
    sizes: {
        height: 186,
        weight: 50,
    }
}

let clone = _.cloneDeep(objects)
```


## Object.assign
---


Копирует все свойства исходный объектов в целевой объект
Возвращает объект `dest`
Если скопированное **свойство** существует - оно будет **перезаписвано**
```js
Object.assign(dest, [src1, src2, src3...])
```
- `dest` - Целевой объект
- `srcN` - Исходные объекты

### Использование
---

1. Создание клонов
```js
Object.assign(user, clone)

clone.name = "Vasya";

alert(`user: ${user.name}`); // "John"
alert(`clone: ${clone.name}`); // "John"
```
или так
```js
let clone = Object.assign({}, user)
```

2. Создание объекта из двух других объектов
```js
let user = { name = "John" };
let permission1 = { canView = true };
let permission2 = { canEdit = true };

// Копирование свойств из permission1, permission2 в user
Object.assign(user, permission1, permission2)
```
3. Глубокое копирование не работает!!

