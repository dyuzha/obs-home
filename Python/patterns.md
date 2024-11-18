## Расширение метода
---
### Плохое решение
```python
class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
        
class KitchenTable(Table)
    def __init__(self, l, w, h, p):
        Table.__init__(self, l, w, h)
        self.places = p
```
**Ошибки**:
- Имя класса может измениться
- Можно ввести любое имя класса (не обязательно наследуемый)

### Хорошее решение
```python
class KitchenTable(Table)
    def __init__(self, l, w, h, p):
        super().__init__(l, w, h)
        self.places = p
```
- В таком случае аргусент *self* в скобках вызываемого родительского метода указывать явно не требуется

### Через `isinstance`
```python
class Table:
    def __init__(self, l=1, w=1, h=1):
        self.length = l
        self.width = w
        self.height = h
        if isinstance(self, KitchenTable):
            p = int(input("Сколько мест: "))
            self.places = p
```

### Классовые методы
```python
class MyClass:
    def __init__(self):
        pass


    @classmethod
    def func(cls, arg: str):
        print(arg)


class YouClass(MyClass):
    @classmethod
    def func(cls):
        super().func("Работает также и с классовыми методами")


```
