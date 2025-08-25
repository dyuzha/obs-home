---
id: cicles_operators
aliases:
  - Циклы и операторы
tags: []
---

# Циклы и операторы
---

## Операторы сравнения
---

 | simbol | Description |
 |--------|-------------|
 | -eq    | =           |
 | -ne    | !=          |
 | -gt    | >           |
 | -ge    | >=          |
 | -lt    | <           |
 | -le    | <=          |

## Условные операторы
---

```ps1
[int]$test = 100
if ($test -eq 100) {
      Write-Host "test = 100"
}



[int]$test = 50
if ($test -eq 100) {
       Write-Host "test = 100"
}
else {
      Write-Host "test <> 100"
}



[int]$test = 10
if ($test -eq 100) {
      Write-Host "test = 100"
}
elseif ($test -gt 100) {
      Write-Host "test > 100"
}
else {
       Write-Host "test < 100"
}



[int]$test = 5
switch ($test) {
     0 {Write-Host "test = 0"}
     1 {Write-Host "test = 1"}
     2 {Write-Host "test = 2"}
     3 {Write-Host "test = 3"}
     4 {Write-Host "test = 4"}
     5 {Write-Host "test = 5"}
     default {Write-Host "test > 5 или значение не определено"}
}
```

## Циклы
---
```ps1
# Циклы с предусловием работают пока/если условие верно
[int]$test = 0
while ($test -lt 10) {
      Write-Host $test
      $test = $test + 1
}

# Циклы с постусловием работают минимум 1 раз

# После работает если истинно
[int]$test = 0
do {
      Write-Host $test
      $test = $test + 1
}
while ($test -lt 10)

# После работает если ложно
[int]$test = 0
do {
      Write-Host $test
      $test = $test + 1
}
until ($test -gt 9)



for ([int]$test = 0; $test -lt 10; $test++) {
       Write-Host $test
}


$test_collection = "item1", "item2", "item3"
foreach ($item in $test_collection)
{
        Write-Host $item
}

```
