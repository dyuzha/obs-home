---
id: map
aliases:
  - Syntax
tags: []
---

[[Commands.md]]

# Syntax
---

`map(<предмет для взаимодействия>, <эффект>)`
- `v:val` - значение текущего элемента

## Object
---
- `String` - примениться к каждому символу
- `List` - примениться к каждому элементу
- `Dict` - примеиться к ключу

## Effect
---
- `v:val "String"` - совершает конкатенацию
-

>[!Example]
```vim
function! Reversed(l)
	let new_list = deepcopy(a:l)
	call reverse(new_list)
	return new_list
endfunction

funcref - переменная, содержащая функцию
function! Mapped(funcref, l)
	let new_list = deepcopy(a:l)
	call map(new_list, string(a:funcref) . '(v:val)')
	return new_list
endfunction

let mylist = [[1, 2], [3, 4]]
echo Mapped(function("Reversed"), mylist)
" >> [[2, 1], [4, 3]]

let fruits = ["apple", "orange", "melon"]
echom map(fruits, 'v:val . " - this is fruits"')
" >> ['apple - this is fruits', `orange - this is ...`]

let list1 = ['1', '2']
echom map(list1, '">" . v:val . "<"')
" >> [`>1<`, `>2<`]

function! Filtered(fn, l)
	let new_list = deepcopy(a:l)
	call filter(new_list, string(a:fn) . '(v:val)')
	return new_list
endfunction

let mylist = [[1, 2], [], ['foo'], []]
echo Filtered(function('len'), mylist)
" >> [[1, 2], ['foo']]

function! Removed(fn, l)
	let new_list = deepcopy(a:l)
	call filter(new_list, '!' . string(a:fn) . '(v:val)')
	return new_list
endfunction

let mylist = [[1, 2], [], ['foo'], []]
echo Removed(function('len'), mylist)
" >> [[], []]
```




