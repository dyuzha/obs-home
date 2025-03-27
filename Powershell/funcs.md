# Функции
---

Для взаимодействия с переменными используется зарезервированная переменная `$args`
Как в функции, так и в сценариях

```ps1
function Get-InfoArgs{
  Write-Host "Arguments count: " $args.count
  Write-Host "Argument 0: " $args[0]
  Write-Host "Argument 1: " $args[1]
}
Get-InfoArgs 0
```

## Param()
---
Для сценария
```ps1
param (
  $arg0, $arg1
)
Write-Host $arg0 $arg1
```

Для функции
```ps1
function test {
    param (
          $arg0, $arg1
    )
    # Body func
}
```


### Доплнительные параметры
---

```ps1
param ( [int]$arg0 )
Write-Host $arg0 $arg1
```

Для функции
```ps1
function test {
    param ( [str]$arg0 )
    # Body func
}
```

#### Атрибут parameter
---
С помощью него можно сделать параметр - обязательным

```ps1
param(
    [parameter(Argument1=value1, Argument2=value2)]
    $ParameterName
)

# Комбинирование
param([parameter(Mandatory=$true)][int]$arg0)

# for func
function test ([parameter(Mandatory=$true)][int]$arg0) { 
}
# or
function test {
    parameter([parameter(Mandatory=$true)][int]$arg0)
}
```

##### Аргумент Alias()
---
Устанавливает псевдоним для параметра
```ps1
param(
    # Параметр обязателен
    [parameter(Mandatory=$true)]
    [alias("ARG","ArgumentName")]
    # Оператор присвоения типов
    [string[]]  # Значение параметра - строковый массив
    $arg0
)
```
##### AllowNull()
---
Разрешает null в качесве значения параметра
```ps1
param(
    [parameter(Mandatory=$true)]
    [AllowNull()]
    [string]
    $arg0
)
```

##### AllowEmptyCollection()
---
Разрешает пустой массив в качестве обязательного параметра:
```ps1
param(
    [parameter(Mandatory=$true)]
    [AllowEmptyCollection()]
    [string[]]
    $arg0
)
```

##### ValidatePattern() 
---
Проверка с использованием регулярного выражения:
```ps1
param(
    [parameter(Mandatory=$true)]
    [ValidatePattern("[0-9][0-9][0-9][0-9]")]
    [string[]]
    $arg0
)
```

##### ValidateLength() 
---
Проверяет длину строкового параметра:
```ps1
param(
    [parameter(Mandatory=$true)]
    [ValidateLength(1,10)]
    [string]
    $arg0
)

```

#### Атрибут position
---
С помощью него можно указать порядок следования аргументов
(*По умолчанию он соответствует порядку объявления*)

```ps1
param(
    [parameter(Mandatory=$true, Position=0)]
    [int]
    $arg0,

    [parameter(Position=1)]
    [string]
    $arg1,

    [parameter(Position=2)]
    [array]
    $arg2
)
```

## Конвейер
---

Получение информации про параметр
```ps1
Get-Help Stop-Process -Parameter Name
```

Через конвейер можно принять значения параметров, для которых установлены соответствующие атрибуты:
- ByValue (*Параметру будет сопоставлен обхъект, в том случае, если его тип соответсвует желаемому*)
- ByPropertyName (*Параметру будет сопоставлено свойство, имя которого будет соответсвовать имени или псевдониму параметра*)

Для установки атрибутов используется parameter() с булевыми аргументами:
- `ValueFromPipeLine`
  Позволяет передать целые объекты через конвейер

- `ValueFromPipeLineByPropertyName`
  Позволяет связать конкретное свойство объекта, переданного через конвейер, с соответсвующим параметром функции


## Структура тела функции
---

```ps1
function test
{
  param()
  begin {}
  process {}
  end {}
}
```

1) Первым однократно запускается `begin {}`
Если параметры передаются в функцию через конвейер, 
  код запуститься до поступления первого объекта на обработку
  `$_` и `$PSitem` в блоке `begin {}` не будут содержать значений

Если параметры указаны явно,
  Перменные будут доступны и в блоке `begin {}`

2) Далее выполняется блок `process {}`
Если параметры переданы через конвейер,
  Данный блок будет запущен поочередно для каждого параметра

Если параметры указаны явно,
  Данный блок будет запущен 1 раз

3) Завершается работа функции однократным выполнением блока `end {}`

> [!Example]
```ps1
function test {
  [CmdletBinding()]
  param(
    [parameter(ValueFromPipeline)]
    [string[]]
    $Param1,

    [string]$Param2
  )

  begin {
    Write-Host "begin: " $Param1
    Write-Host "begin: " $Param2
  }

  process {
    Write-Host "proc: " $Param1
    Write-Host "proc: " $Param2
  }

  end {
    Write-Host "End"
    Write-Host "pipeline: " $Param1
    Write-Host "arg: " $Param2
    }
}
'1', '2', '3' | test -Param2 '4'
```

## CmdletBinding()
---
Инициализирует новый объект класса `CmdletBindingAttribute`, через вызов конструктора, которому можно передавать необязательные аргументы

`-Force` применяется для подавления запросов на проведение различных операций
`-Whatif` используется для отображения информации о последствиях функции/команды без этого действия
  Обчычно используется, если функция может выполнить деструктивные действия



