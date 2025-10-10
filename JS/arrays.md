---
id: arrays
aliases:
  - arrays
  - array
tags: []
---
**Back**
    [[!JS]]

# array
---
Массив - это **ОБЪЕКТ**

```js
let att = new Array();
let arr = []
```
```js
let arr = ['Яблоко', {name: 'Джон'}, true, fynction() {alert('Привет')}]

alert(arr[1].name); // Джон
arr[3](); //  Привет
```
**Отрицательных индексов - нет**
```js
alert(fruits[fruits.length-1]); // Привет
alert(fruits.at(-1)); // Привет
```

## Методы
---
```js
let fruits = ["Яблоко", "Апельсин", "Слива"];

alert(fruits); // Яблоко, Апельсин, Слива
```

Двустороняя очередь
```bash
[Slow]                      [Fast]
shift   ->                  pop ->
            0 | 1 | 2 | 3
undhift <-                  push <-
```
`shift` - Добавить элемент в начало
`unshift` - Удалить элемент из начала (и получить)
`pop` - Удалить элемент из конца (и получить)
`push` - Добавить элемент в конец
```js
let fruits = ["Apple"]

fruits.push("Orange", "Pineapple")
fruits.unshift("Pine", "Lemon")
```

## Поведение (как у объектов)
---
```js
let fruits = ["Banana"]

let arr = fruits; // Копируется по ссылке (две переменные ссылаются на один и тот же объект)

alert (arr === fruits); //true

arr.push("Pineapple");

alert(fruits); // Banana, Pineapple
```

В случае обращения с массивом как с обычным объектом, все его фичи по оптимизации будут отключены

```js
let fruits = [];

fruits[9999] = 6;
fruits.age = 25;
```

## Собственный вариант цикла for
---
```js
let fruits = ["Яблоко", "Апельсин", "Слива"];

for (let fruit of fruits) {
    alert(fruit);
}

// в 10-100 раз медленее чем for ... of ...
// Так как это массив, можно получить его ключи (индексы)
// Если у объекта (псевдомассива) есть и другие ключи, они будут использованы
for (let key in arr) {
    alert(arr[key]);
}
```

## length
---
Свойство `length` автоматически обновляется при изменении массива.
- Это количество **не элементов массива** а наибольший индекс +1.
```js
let fruits = [];
fruits[123] = "Apple";

alert(fruits.length); 124
```
Если уменьшить свойство length, массив потеряет элементы (которые не поместятся в новую длину) Безвозвратно
```js
let arr = [1, 2, 3, 4, 5]

arr.length = 2;
alert(arr); // [1, 2]

arr.length = 5;
alert(arr[3]); // undefined
```
Самый простой способ очистить массив - arr.length = 0


