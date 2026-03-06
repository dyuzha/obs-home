# Типы данных
---

## Массивы
---

```ps1
$test_array = @() # Пустой массив
$test_array = @(1, 2, 3, 4) # создаем массив из четырех элементов 
$test_array = 1, 2, 3, 4 # Оператор @ можно опуcтить
$test_array = , 1 # Массив из одного элеменаи

# Обращение по индексу
$test_array[0] = 1

# Можно указывать несколько индексов через запятую
$test_array = "один", "два", "три", "четыре"
$test_array[0,1,2,3]
$test_array[1,1,3,3,0]

$test_array[0..100] # Если диапазон больше массива - возвращаются все значения
$test_array[-1..0]
# Если попытаться обратиться к единственному несуществующему элементу массива, возвращается значение $null.

$test_array.count # -> 4

# Строготипизированный массив
[int[]]$test_array = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

### Диапазоны
---
```ps1
1..4 # -> 1, 2, 3, 4
```

## Хеш-таблицы 
---

```ps1
$test_hashtable = @{} # Пустая хеш-таблица
$test_hashtable = @{one="один"; two="два"; three="три"; "some key"="some value"}

# Обращение к элементам таблицы
$test_hashtable."some key"
$test_hashtable["some key"]
$test_hashtable.one

# Добавление элемента в таблицу (присваивается не существующие значение)
$test_hashtable.Add("four", "четыре")
$test_hashtable.five = "пять"
$test_hashtable['five'] = "заменяем значение"
$test_hashtable.Remove("one")
```

## Функции
---
Функция всегда возвращает результат 
Если вернуть надо более одного значения - это массив
```ps1
function funcName (arg1, ..., argN) 
{ 
  # Body func
} 
# Пример создания функции
function sqr ($number)
{
      return $number * $number
}

# Вызов функции
sqr 2 
# or
aqr -number 2

# Из-за способа передачи аргументов саму функцию приходится заключать в скобки
function test_func ($n) {}
test_func -eq $null     # функция не вызывалась
(test_func) -eq $null   # результат выражения — $true

# При описании функции можно присваивать значение по умолчанию
function func ($arg = value) {
         #тело функции
}
```

## Обработка ошибок
---
```ps1
try {
    [int]$test = Read-Host "Input number: "
    100 / $test
} catch {
    Write-Warning "Incorrect number"
} finally {
    Write-Host "End."
}

```

