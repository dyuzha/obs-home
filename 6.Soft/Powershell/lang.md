## Переменные
Динамическая типизация
Перменные в PS - это полноценные объекты (классы) имеющие:
- свойства
- методы
```ps1
# Можно использовать 2 варианта
[int]$number = 100
$number = [int]100

# System.String
[str]$string = 100

# System.Bool
[bool]$string = $true

# System.Int32
[int]$number = 123456789

# System.Int64
[long]$number = 12345678910

# System.Single - 32 бита
[single]$float = 12345,6789

# System.Double - 64 бита
[double]$float = 123456789,101112

# System.Decimal - 128 бита
[decimal]$float = 12345,689d

# System.DateTime 
[DateTime]$date = Get-Date

# System.Object
[array]$list = 1, 2, "string", 4

# System.Collections.Hashtable
[hashtable]$dict = @{one="1"; two="2"}
```

### Функции для взаимодействия с пермененными
---
```ps1
# Узнать тип переменной
$test.GetType().FullName

# Вывести команды для управления переменными
Get-Command -Noun Variable | ft -Property Name, Definition -AutoSize -Wrap

# Вывести объявленные переменные и их значения
Get-Variable | more
```
### Системные переменные
---
Не удаляются после текущего сеанса

```ps1
$PWD.Path
```
Для хранения пользовательских настроек нужны переменные предпочтений
(*Значение которых можно изменить*)
К примеру, с помощью `$ErrorActionPreference` задается реакция интерпретатора команд на возникновение некритических ошибок.

Для обращения к объявленным переменным существует псевдонакопитель `Variable`
Работать с ним можно по аналогии с другими накопителями
Переменные напоминают объекты файловой системы

```ps1
Get-ChildItem Variable: | more
# or
ls Variable: | more
```

## Области видимости
---
**Global**  - Все переменные сеанса (н-р системные переменные)
**Local**  - Доступны только в той области, для которой были определены (н-р в функции)
**Сценарий**  - Для команд скрипта, по сути является локальной областью

```ps1
# Задать глобальную переменную
$Global:test = 100
```

## Переменные окружения (среды)
---
`Env` - псевдонакопитель для обращения к переменным среды
(*При запуске оболочки - они копируются из родительского процесса*)

```ps1
# Посмотреть переменные окружения
dir Env: # or
ls Env: # or
Get-ChildItem Env:
```

Командлеты `*-Variable` с переменными среды не работают
(*Чтобы их использовать, необходимо использовать префикс диска*)
```ps1
$env:test = "Hello world"
$env:test # Вывести на экран
```

## Операторы сравнения
---

simbol | Description
---    |---
-eq    | =
-ne    | !=
-gt    | >
-ge    | >=
-lt    | <
-le    | <=

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

# После работает пока истинно
[int]$test = 0
do {
      Write-Host $test
      $test = $test + 1 
}
while ($test -lt 10)

# После работает пока ложно
[int]$test = 0
do {
      Write-Host $test
      $test = $test + 1 
}
until ($test -gt 9)
```
## Переменные
Динамическая типизация
Перменные в PS - это полноценные объекты (классы) имеющие:
- свойства
- методы
```ps1
# Можно использовать 2 варианта
[int]$number = 100
$number = [int]100

# System.String
[str]$string = 100

# System.Bool
[bool]$string = $true

# System.Int32
[int]$number = 123456789

# System.Int64
[long]$number = 12345678910

# System.Single - 32 бита
[single]$float = 12345,6789

# System.Double - 64 бита
[double]$float = 123456789,101112

# System.Decimal - 128 бита
[decimal]$float = 12345,689d

# System.DateTime 
[DateTime]$date = Get-Date

# System.Object
[array]$list = 1, 2, "string", 4

# System.Collections.Hashtable
[hashtable]$dict = @{one="1"; two="2"}
```

### Функции для взаимодействия с пермененными
---
```ps1
# Узнать тип переменной
$test.GetType().FullName

# Вывести команды для управления переменными
Get-Command -Noun Variable | ft -Property Name, Definition -AutoSize -Wrap

# Вывести объявленные переменные и их значения
Get-Variable | more
```
### Системные переменные
---
Не удаляются после текущего сеанса

```ps1
$PWD.Path
```
Для хранения пользовательских настроек нужны переменные предпочтений
(*Значение которых можно изменить*)
К примеру, с помощью `$ErrorActionPreference` задается реакция интерпретатора команд на возникновение некритических ошибок.

Для обращения к объявленным переменным существует псевдонакопитель `Variable`
Работать с ним можно по аналогии с другими накопителями
Переменные напоминают объекты файловой системы

```ps1
Get-ChildItem Variable: | more
# or
ls Variable: | more
```

## Области видимости
---
**Global**  - Все переменные сеанса (н-р системные переменные)
**Local**  - Доступны только в той области, для которой были определены (н-р в функции)
**Сценарий**  - Для команд скрипта, по сути является локальной областью

```ps1
# Задать глобальную переменную
$Global:test = 100
```

## Переменные окружения (среды)
---
`Env` - псевдонакопитель для обращения к переменным среды
(*При запуске оболочки - они копируются из родительского процесса*)

```ps1
# Посмотреть переменные окружения
dir Env: # or
ls Env: # or
Get-ChildItem Env:
```

Командлеты `*-Variable` с переменными среды не работают
(*Чтобы их использовать, необходимо использовать префикс диска*)
```ps1
$env:test = "Hello world"
$env:test # Вывести на экран
```
