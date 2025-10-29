---
id: map
aliases:
  - Map
tags: []
---
**Back**
    [[!JS]]

# Map
---
Это коллекция ключ-значение, как и объект, но основное отличие, что ключи мб любого типа.

```js
new Map() // Создает коллекцию
map.set(key, value) // Записывает по ключу, значение
map.get(key) // Возвращает значение по ключу
map.has(key) // Возвращает true, если ключ существует, иначе false
map.delete(key) // Удаляет элемент (пару: ключ-значение) по нлючу
map.clear() // Очищает коллекцию от всех элементов
map.size() // Возвращает текущее количество элементов
```
Для перебора
```js
map.values()
map.keys()
map.entryis() // Аналог items() в Py

// Также можно использовать сам map
for (let entry of recipeMap) { // то же самое, что и recipeMap.entries()
  alert(entry); // key,value
}

// выполняем функцию для каждой пары (ключ, значение)
recipeMap.forEach((value, key, map) => {
  alert(`${key}: ${value}`); // огурец: 500 и так далее
});
```

```js
let map = new Map();

map.set("1", "str1");    // строка в качестве ключа
map.set(1, "num1");      // цифра как ключ
map.set(true, "bool1");  // булево значение как ключ

// *обычный объект Object приводит ключи к строкам*
// Map сохраняет тип ключей, так что в этом случае сохранится 2 разных значения:
alert(map.get(1)); // "num1"
alert(map.get("1")); // "str1"

alert(map.size); // 3
```

> [!INFO] Сравнение ключей
> Чтобы сравнивать ключи, объект Map использует алгоритм SameValueZero. Это почти такое же сравнение, что и ===, с той лишь разницей, что NaN считается равным NaN. Так что NaN также может использоваться в качестве ключа.


Каждый вызов `map.set()` возвращает объект map, так что можно объеденить их в цепочку.
```js
map.set('1', 'str1')
    .set(1, 'num1')
    .set(true, 'bool1')
```

## Создание
---
Из массива
```js
// массив пар [ключ, значение]
let map = new Map([
  ['1',  'str1'],
  [1,    'num1'],
  [true, 'bool1']
]);
```

Из объекта
```js
let obj = {
  name: "John",
  age: 30
};

let map = new Map(Object.entries(obj));
```

Создание объекта из map
```js
let map = new Map();
map.set('banana', 1);
map.set('orange', 2);
map.set('meat', 4);

let obj = Object.fromEntries(map.entries()); // создаём обычный объект (*)
```
