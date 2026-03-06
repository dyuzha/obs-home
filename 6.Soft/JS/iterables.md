---
id: iterables
aliases:
  - iterables
tags: []
---

# iterables
---

## Symbol.iterator
---
```js
let range = {
    from: 1,
    to: 5
};

range[Symbol.iterator] = function() {
    return {
        current: this.from,
        last: this.to,

        next() {
            if (this.current <= this.last) {
                return {done: false, value: this.current++};
            } else {
            return {done: false};
            }
        }
    };
};

// Можно упростить и возвращать сам объект в качестве итератора
let range = {
  from: 1,
  to: 5,

  [Symbol.iterator]() {
    this.current = this.from;
    return this;
  },

  next() {
    if (this.current <= this.to) {
      return { done: false, value: this.current++ };
    } else {
      return { done: true };
    }
  }
};

for (let num of range) {
  alert(num); // 1, затем 2, 3, 4, 5
}


for (let num of range) {
    alert(num); //1, 2, 3, 4,
}
```
Когда цикл `for ... of` запускается, он вызывает метод Symbol.iterator 1 раз.
1. Если метод не найден, возвращается ошибка
2. Если найден, возвращается объект с методом `next`
3. `next()` должен {done: Boolen, value: any}, где `done=true` означает, что цикл завершен

## Array.from()
---
Универсальный метод, который принимамет итерируемый объект или псевдомассив и делает из него "Настоящий" `Array`.
Также применяет опционально функцию для применения к каждому элементу перед добавлением в массив.
После этого можно использовать методы массивов, такие как pop(), shift() и тд.
```js
// возводим каждое число в квадрат
let arr = Array.from(range, num => num * num);

alert(arr); // 1,4,9,16,25
```


## Нейминг
---
Итерируемые объекты - объекты имеющие `Symbol.iterator`
Псевдомассивы - объкеты, реализующие индексацию и length (строки).


## Перебор
---
Методы для структур данных (возвращают итерируемые объекты):
- keys()
- values()
- entries()

Методы для объектов (возврашают массив):
- Object.keys(obj) - возвращает ключи (имена свойств) (игнорируют символьные свойства)
- Object.values(obj) - возвращает значение (игнорируют символьные свойства)
- Object.entries(obj) - возвращает пары ключ значение (двумерный массив) (игнорируют символьные свойства)

- Object.getOwnPropertySymbols(obj) - возвращает массив только символьных ключей
- Reflect.ownKeys(obj) - возвращает все ключи (включая символьные)

Трансформация объектов.


