---
id: cicles
aliases:
  - Циклы
tags: []
---
**Back**
    [[!JS]]

# Циклы
---

## While
---

### С предусловием
---
```js
while (condition) {
    // body
}

let i = 0;

// Многострочный вариант
while (i < 3){
    alert(i++);
}

// Для однострочных: {} не требуются
while (i < 3) alert(i++);
```

### С постусловием
---
- Если нужно, чтобы в случае, что условие ложно: тело выполнилось один раз.
- Или если условие будет ясно только входе выполнения цикла
```js
let i = 0;

do {
   alert(i++);
} while (i <3);
```

## For
---
```js
for (let i = 0; i < 3; i++) {
    alert(i)
}

for (;;) {
  // будет выполняться вечно
}

```

## Break
---
Преждевременный выход из цикла
```js
let sum = 0;

while (true) {
   let value = +prompt("Input number", "");
    if (!value) break;
    sum += value;
}

alert(`summ: ${sum}`);
```

## Continue
---
Преждевременный переход к сл. итерации

```js
for (let i = 0; i < 10; i++) {
    if (i % 2 == 0) continue;
    alert(i); // 1, 3, 5, 7, 9
}
```

## Метки (label)
---
Позволяют разорвать цикл(ы) до определенной метки
```js
outer:
for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        let input = prompt(`Значение на координатах (${i},${j})`, '');
       if (input) break outer;
    }
}

alert("Выход из циклов")
```

Или передать управление в произвольное место в коде (при помощи `continue`)

## Cases
---
Проверка на равенство всегда строгая `===`
```js
switch (key) {
    case value1:
        // ...
        break;

    case value1:
        // ...
        break;

    case value1:
        // ...

    default:
        break;
}
```
Если в одном из "case" нет default, то при срабатывании этого варианта, код пойдет ниже, пока не встретит default
