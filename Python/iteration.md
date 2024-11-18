**Back**
	[[Python]]
# Итератор
---
- Это объект, реализующий в себе интерфейс перебора чего-либо.
(Он содержит правило перебора)

Цикл `for` в действительности взаимодействует не с самой коллекцией, а с итератором объекта коллекции
- Он неявно вызывает функцию `iter`
    `iter(obj)`

**Обход через цикл For**
```python
tumb = ["ножницы", "карандаш", "яблоко", "книга"]
for item in tumb:
    print(item)
```

**Через цикл while**
```python
tumb = ["ножницы", "карандаш", "яблоко", "книга"]
iterator = iter(tumb)

try:
    while True:
        next_val = next(iterator)
        print("Очередное значение:", next_val)
except StopIteration:
    print("Stop iteration")
print("Stop program")
```
**Самописный Итератор**
```python
class Tumbochka:
    """ Magic tumbochka with 3 character """

    def __init__(self):
        self.boxes = {
            1: [],
            2: [],
            3: []
        }

    def add_to_box(self, obj, box_num):
        if box_num not in {1, 2, 3}:
            raise NameError("Неправильное имя ящика")
        else:
            self.boxes[box_num].append(obj)

    def remove_from_box(self, box_num):
        if box_num not in {1, 2, 3}:
            raise NameError("Неправильное имя ящика")
        else:
            return self.boxes[box_num].pop()

    def __str__(self):
        boxes_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
        return ", ".join(boxes_items)

    def __iter__(self):
        boxes_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
        it = iter(boxes_items)
        return it
```

**Генератор**
```python
def __iter__(self):
    boxes_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
    for elem in boxes_items:
        yield elem, id(elem)
```

**Кастомный генератор** позволяет *тонко управлять процессами перебора*, 
н-р: 
- возможность при каком-то событии начать итерацию с начала
- или установить значение указателя перебора на определенный элемент

**Кастомный генератор это отдельный класс**

```python
    def __iter__(self):
        return TumbIterator()


class TumbIterator:
    def __next__(self):
        pass

print(iter(tumb)) # >>> <main.TumbIterator object at 0x10...>
iterator = iter(tumb)
print(next(iterator)) # >> None
print(next(iterator)) # >> None
print(next(iterator)) # >> None
```
