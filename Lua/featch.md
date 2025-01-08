---
id: featch
aliases: []
tags: []
---

Back
[[Reference]]

# Feeatch
---

## Tostring
---
Преобразовывает значение любого типа (кроме таблиц) в строку
```lua
local a = tostring (10) --  "10"
local b = tostring (true) --  "true"
local c = tostring (nil) --  "nil"

-- Содержание таблиц функцией tostring не преобразуется
local d = tostring ({ [1] = "это поле 1" }) -- d равно "table: 06DB1058"

print(a, b, c, d)
```


## Render
---

