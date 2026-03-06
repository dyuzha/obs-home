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

### Добавление удаление эллементов
---
`arr.fill(value, start, end)`
 заполняет массив повторяющимися value, начиная с индекса start до end.


Оператор `delete` (Как у объекта)
```js
let arr = ["I", "go", "home"];

delete arr[1]; // удалить "go"

alert( arr[1] ); // undefined

// теперь arr = ["I",  , "home"];
alert( arr.length ); // 3
```

`arr.splice`
```js
arr.splice(start[, deleteCount, elem1, ..., elemN])

let arr = ["I", "Go", "Home"];
arr.splice(1, 1); // Начиная с индекса 1, удалить 1 элемент
allert(arr); // "I", "Home"

let arr = ['I', 'learning', 'JS', 'just', 'now' ]

// Начиная с 0 индекса улаоить 3 элемена, в этот промежуток добавить "Давай", "танцевать"
arr.splice(0, 3, "Давай", "танцевать");
allert(arr); // Давай танцевать just now

// Вставление элементов без удаления
arr.splice(2, 0, "сложный", "язык");
```
`arr.slice`
Возвращает новый массив, в котором скопированны все элементы с start по end (не включая)
```js
arr.slice([start], [end])

let arr = ["t", "e", "s", "t"];

alert( arr.slice(1, 3) ); // e,s (копирует с 1 до 3)

alert( arr.slice(-2) ); // s,t (копирует с -2 до конца)
```
`arr.concat`
Объединяет массивы (путем создания нового массива и копированием туда элементов)
```js
arr.concat(arg1, arg2...)
```

Обычно он копирует только элементы из массивов.
Другие объекты, даже если они выглядят как массивы, добавляются как есть:
```js
let arr = [1, 2];

let arrayLike = {
  0: "что-то",
  length: 1
};

alert( arr.concat(arrayLike) ); // 1,2,[object Object]
```
…Но если массивоподобный объект имеет специальное свойство Symbol.isConcatSpreadable, то он обрабатывается как массив, с помощью concat: вместо него добавляются его элементы:
```js
let arr = [1, 2];

let arrayLike = {
  0: "что-то",
  1: "ещё",
  [Symbol.isConcatSpreadable]: true,
  length: 2
};

alert( arr.concat(arrayLike) ); // 1,2,что-то,ещё
```

`arr.forEach()`
```js
arr.forEach(function(item, index, array) {
  // ... делать что-то с item
});
Результат функции (если она что-то возвращает) отбрасывается и игнорируется.
```



#### Двустороняя очередь
---
```bash
[Slow]                      [Fast]
shift   ->                  pop ->
            0 | 1 | 2 | 3
undhift <-                  push <-
```
`arr.shift` - Добавить элемент в начало
`arr.unshift` - Удалить элемент из начала (и получить)
`arr.pop` - Удалить элемент из конца (и получить)
`arr.push` - Добавить элемент в конец
```js
let fruits = ["Apple"]

fruits.push("Orange", "Pineapple")
fruits.unshift("Pine", "Lemon")
```

### Поиск
---
`arr.find(function(item, index, array))`
Ищет первый элемент, который заставит функцию вернуть `true`.

```js
let result = arr.find(function(item, index, array));
let result = arr.find((item, index, array) -> { ... })

let users = [
{id: 1, name: "Petya"},
{id: 2, name: "Sasha"},
{id: 3, name: "Vasya"},
];

let firstUser = users.find(item => item.id == 1);

// Аналог
let firstUser = users.find(function(item) {
    return item.id == 1
})

alert(firstUser.name);
```

Если найденных элементов мб много, тогда можно использовать `arr.filter()`
`arr.filter()`
Синтаксис такой же, но возвращает массив из найденных элементов.


`arr.indexOf()`
Ищет индекс `itemForFind` начиная с `FromIndex`, возращает `idex` или -1
```js
// Если fromIndex отрицательный, он интерпретируется как:
// (но поиск всё равно идёт слева направо)
fromIndex = arr.length + fromIndex
```
`arr.lastIndexOf()`

`arr.includes()`
Ищет `itemForFind` начиная с `FromIndex`, возвращает `bool`
```js
arr.includes(itemForFind [, FromIndex]) // -> bool
// valForFind искомый элемент
// FromIndex (opt) с какого индекса искать
```

#### thisArg
----
```js
arr.find(func, thisArg);
arr.filter(func, thisArg);
arr.map(func, thisArg);
// ...
// thisArg -- необязательный последний аргумент
```
Значение парметра `thisArg` становиться `this` для `func`.
```js
let army = {
  minAge: 18,
  maxAge: 27,
  canJoin(user) {
    return user.age >= this.minAge && user.age < this.maxAge;
  }
};

let users = [
  {age: 16},
  {age: 20},
  {age: 23},
  {age: 30}
];

// найти пользователей, для которых army.canJoin возвращает true
let soldiers = users.filter(army.canJoin, army);
let soldiers = users.filter(user => army.canJoin(user))

alert(soldiers.length); // 2
alert(soldiers[0].age); // 20
alert(soldiers[1].age); // 23
```







### Преобразование
---
`arr.map`
Вызывает функцию для каждого элемента массива и возвращает массив результатов выполнения этой функции.
```js
let result = arr.map(function(item, index, array) {
  // возвращается новое значение вместо элемента
});

// Например, преобразовать каждый элемент массива в его длинну
let lengths = ["Бильбо", "Гэндальф", "Назгул"].map(item => item.length);
alert(lengths); // 6,8,6
```

`arr.sort`

По умолчанию элементы сортируются как строки.
```js
let arr = [ 1, 2, 15];
arr.sort()
allert(arr); // 1, 15, 2
```
```js
[1, -2, 15, 2, 0, 8].sort(function(a, b) {
  alert( a + " <> " + b );
  return a - b;
});

arr.sort(function(a, b) { return a - b; });

// localeCompare для строк
let countries = ['Österreich', 'Andorra', 'Vietnam'];

alert( countries.sort( (a, b) => a > b ? 1 : -1) ); // Andorra, Vietnam, Österreich (неправильно)

alert( countries.sort( (a, b) => a.localeCompare(b) ) ); // Andorra,Österreich,Vietnam (правильно!)
```

`arr.reverse`
Меняет порядок `arr` на обратный
```js
let arr = [1, 2, 3, 4, 5];
arr.reverse();

alert( arr ); // 5,4,3,2,1
```

`arr.reduce`
Используется для вычисления единого значения на основе всего массива.
```js
let value = arr.reduce(function(accumulator, item, index, array){
    //...
}, [initial]);
```
Функция применяется по очереди ко всем элементам массива и "переносит" свой результат на следующий вызов.
**accumulator**  - результат предыдущего вызова этой функции, равен initial при первом вызове (если initial передан)
**item** - очередной элемент массива
**index** - позиция очередного элемента
**array** - весь массив
```js
let arr = [1, 2, 3, 4, 6, 7, 8, 10];

// Выводит сумму массива
let result = arr.reduce((summ, current) => summ + current, 0);

// Аналогичный результат
let result = arr.reduce((summ, current) => summ + current);
```
> [!IMPORTANT]
> При отсутствии initial в качестве первого значения берётся первый элемент массива, а перебор стартует со второго.

`arr.reduceRight`
Аналогичено `reduce`, но с права на лево.

### Создание
---
Создание из строк
`str.split(delim)`
```js
let names = 'Vasya, Petya, Lolya';
let arr = names.split(', ');

for (let name of arr) {
    alert(`Сообщения получит ${name}:`)
}

let arr = names.split(', ', 2); // Указал количество элементов в результативном массиве
alert(arr); // Vasya, Petya

let str = 'test';
alert(str.split('')); // t,e,s,t
```
Обртный метод
`arr.join(glue)`
```js
let arr = ['Вася', 'Петя', 'Маша'];

let str = arr.join(';'); // объединить массив в строку через ;

alert( str ); // Вася;Петя;Маша
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

`Array.isArray()`
Так как поведение как у объектов, то
```js
alert(typeof {}); // object
alert(typeof []); // object

Array.isArray({}); // false
Array.isArray([]); // true
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
